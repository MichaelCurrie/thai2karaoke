"""
thai_parser: A Thai abugida text codec

A custom text codec for encoding and decoding strings drawn from the
Thai abugida into romanized "Karaoke" strings.

The design philosophy here is to use a data-based approach.  So instead of 
hardcoding the pronunciation rules into the code, we load a metadata file,
thai.csv, using `pandas`, and then use the `codec` library to create standard
encoding and decoding semantics.

About the Thai abugida
======================

The Thai abugida, said to have been invented by King Ramkhamhaeng the Great
around 1283, consists of words consisting of syllables, which are composed
of consonants surrounded by vowels and tone markings.

The Unicode block for Thai is from code points 0xE00 to 0xE7F.

Of the 128 graphemes in that range:
    44 are consonants (of which two, ฃ and ฅ, are obsolete)
    41 are left unassigned
    10 are the Thai numerals from 0 to 9
    19 are vowels
    4 are tone markers (่, ้, ๊, ๋)
    4 are diacritics
        ็ shortens the vowel
        ฺ indicates that the vowel should not be pronounced
        ์ indicates a silent letter
        ๎ "yamakkan", from Sanskrit (obsolete)
    6 are symbols
        ๆ indicates that the preceding word should be duplicated
        ฿ Thai Baht currency symbol
        ฯ end of sentence
        ๏ end of paragraph (obsolete)
        ๚ end of chapter
        ๛ end of document

Rules
=====
See http://www.thai-language.com/id/830221

Every syllable consists of:
1. Preposed vowel (optional)
2. Initial consonant
3. Implied vowel (optional)
4. Postposted, superposed, or subposed vowels (optional)
5. Consonants ย, ว, or อ appearing as part of a compound vowel (optional)
6. Tone marker (optional)
7. Final consonant (optional)
- Diacritics (currently removed from parsed text)

e.g. เตียง
preposed_vowels = เ
initial_consonant = ต
later_vowels = ีย
final_consonant = ง


Usage
=====

>>> import thai_parser
>>> 'กับ'.encode('karaoke')
kab
>>> 'sawadee krub'.decode('karaoke')
สวัสดีครับ

Testing
=======

# Since example_thai.txt and example_karaoke.txt are a list of examples that
# are designed to be exactly the same:

>>> with open('example_thai.txt', 'r') as ex_thai, open('example_karaoke.txt', 'r') as ex_karaoke:
...     assert(ex_thai.read().encode('karaoke') == ex_karaoke.read())

>>> with open('example_thai.txt', 'r') as ex_thai, open('example_karaoke.txt', 'r') as ex_karaoke:
...     assert(ex_karaoke.read().decode('karaoke') == ex_thai.read())

>>> # Double conversion should leave the text unchanged
>>> with open('example_thai.txt', 'r') as ex_thai:
...     thai_text = ex_thai.read()
...     assert(thai_text.encode('karaoke').decode('karaoke') == thai_text

# TODO: test the syllable parser explicitly.

"""

import pandas as pd


class thai_consonant:
    @property
    def consonant_class(self):
        pass

    @property
    def is_dead(self):
        """ Also known as 'plosive', as opposed to live, or 'sonorant'
        Returns boolean
        """
        pass

class thai_vowel:
    @property
    def is_long(self):
        # TODO
        return False


class thai_syllable:
    thai_string = ''

    @property
    def initial_consonants(self):
        return ''

    @property
    def has_initial_consonant_cluster(self):
        pass

    @property
    def ending_consonant(self):
        pass

    @property
    def initial_consonant(self):
        pass

    @property
    def vowel(self):
        pass

    @property
    def tone(self):
        if self.tone_mark_exists:
            if self.tone_mark == '่':
                if self.initial_consonant.consonant_class == 'low':
                    if self.vowel.is_long:
                        return 'falling'
                    else:
                        return 'high'
                else:
                    return 'low'
            elif self.tone_mark == '้':
                if self.initial_consonant.consonant_class == 'low':
                    return 'high'
                else:
                    return 'falling'
            elif self.tone_mark == '๊':
                return 'high'
            elif self.tone_mark == '๋':
                return 'rising'
        else:
            if not self.ending_consonant:
                if self.vowel.is_long:
                    if self.initial_consonant.consonant_class == 'high':
                        return 'rising'
                    else:
                        return 'mid'
                else:
                    if self.initial_consonant.consonant_class == 'low':
                        return 'rising'
                    else:
                        return 'mid'

thai = pd.read_csv('thai.csv', ';')

PREPOSED_VOWELS = thai[
    thai["Grapheme position"] == "preposed"]["Symbol"].values

def parse_string(s):
    """ Take string of Thai text s and return an array of syllables
    """
    # First check that all characters are Thai
    for c in s:
        if not 0xe00 < ord(c) < 0xe80:
            raise Exception('This is not Thai text')

    s_arr = []

    i = 0
    current_start = 0
    initial_consonant = ''
    vowel = ''
    final_consonant = ''
    while i < len(s):
        cur_type = thai[thai["Symbol"] == s[i]]["Type"].values[0]

        if cur_type == "Consonant":
            if initial_consonant == '':
                initial_consonant = s[i]
                i += 1
                continue
            else:
                if vowel == '':
                    initial_consonant = initial_consonant + s[i]
                    i += 1
                    continue
                else:
                    final_consonant = s[i]
                    s_arr.append(s[current_start:i+1])
                    i += 1
                    current_start = i                    
                    continue
        elif cur_type == "Vowel":
            vowel = s[i]
            i += 1
            continue

exs1 = 'กับ'   # "For"
exs2 = 'กับกับ'  # just a doubling of the first example 
exs3 = 'ควาย'  # Buffalo
