# Thai parser
# Converts Thai characters to roman "karaoke" characters
# The design philosophy here is to use a data-based approach

"""
The Thai abugida, said to have been invented by King Ramkhamhaeng the Great
around 1283, consists of words consisting of syllables, which are composed
of consonants surrounded by vowels and tone markings.

Test the parser against a pre-loaded set of Thai words broken into syllables

The Unicode block for Thai is U+0E00–U+0E7F.  Of the 128 character slots,
44 are consonants

TODO: make this into a formal "encoding" so you can encode a string of Thai
characters with .encode('thai_karaoke') and get back the karaoke encoding!


"""

import pandas as pd

def parse_string(s):
    """ Take string of Thai text s and return an array of syllables
    """
    # First check that all characters are Thai
    for c in s:
        if not 0xe00 < ord(c) < 0xe80:
            raise Exception('This is not Thai text')

    return [s]





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








