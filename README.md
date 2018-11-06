# thai2karaoke

thai_parser: A Thai abugida text codec

A custom text codec for encoding and decoding strings drawn from the
Thai abugida into romanized "Karaoke" strings.

### Usage

    >>> import thai_parser
    >>> 'กับ'.encode('karaoke')
    kab
    >>> 'sawadee krub'.decode('karaoke')
    สวัสดีครับ

### About this repo

The design philosophy here is to use a data-based approach.  So instead of 
hardcoding the pronunciation rules into the code, we load a metadata file,
thai.csv, using `pandas`, and then use the `codec` library to create standard
encoding and decoding semantics.

### About the Thai abugida

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
Every syllable consists of:
1. Preposed vowel (optional)
2. Initial consonant
3. Implied vowel (optional)
4. Postposted, superposed, or subposed vowels (optional)
5. Consonants ย, ว, or อ appearing as part of a compound vowel (optional)
6. Tone marker (optional)
7. Final consonant (optional)
- Diacritics (currently removed from parsed text)

Works cited
===========

Worapong Khumthong ("ComdevX").  For the original Javascript thai2karaoke repository. 

thai-language.com, by [Glenn Slayden](https://www.linkedin.com/in/glennslayden/).  http://www.thai-language.com/id/830221

Siripong Potisuk.  Prosodic Annotation in a Thai Text-to-speech System.  http://www.aclweb.org/anthology/Y07-1042

Wirote Aroonmanakun.  Thoughts on word and sentence segmentation in Thai.  https://www.researchgate.net/publication/27808921_Thoughts_on_word_and_sentence_segmentation_in_Thai

Chart of Thai tone rules.  http://womenlearnthai.com/index.php/finding-the-tone-of-a-thai-syllable/

Syllables of the Thai language.  Theo Pitsch.  http://www.clickthai-online.com/basics/syllables.html

Brian Ray.  Parsing a custom syntax with a finite state machine (FSM).  https://medium.com/@brianray_7981/tutorial-write-a-finite-state-machine-to-parse-a-custom-language-in-pure-python-1c11ade9bd43

Thai word list.  https://lingopolo.org/thai/words-by-frequency


Original documentation:
=======================
Project: thai2karaoke<br />
Created: Comdevx<br />
Email: comdevx@gmail.com<br />
Started: 2017/08/04 21.00<br />
Facebook: http://www.fb.com/comdevx<br />
<br />
สามารถสนับสนุนได้นะครับ<br />
BTC: 13owVDCcYykj853S5W37Ys7np97jvCtL7Z<br />
ETH: 0xa751F70e862E3747e435430105bbE6db20C828C9<br />
LTC: LNP95PsUgtzYghK5Ada7w3hHK2WwEYSSwn<br />
XRP: rp7Fq2NQVRJxQJvUZ4o8ZzsTSocvgYoBbs<br />
<br />
สามารถดัดแปลงแก้ไขทำเพิ่มเติมได้ แต่ขอแค่มีเครดิตไว้ให้หน่อยก็ดีครับ<br />
<br />
แหล่งอ้างอิง<br />
https://th.wikipedia.org/wiki/การถอดอักษรไทยเป็นอักษรโรมันแบบถ่ายเสียงของราชบัณฑิตยสถาน<br />
<br />
convert thai language to karaoke (Romanization)<br />
<br />
word list number<br />
0 'ก'
1 'ข'
2 'ฃ'
3 'ค'
4 'ฅ'
5 'ฆ'
6 'ง'
7 'จ'
8 'ฉ'
9 'ช'
10 'ซ'
11 'ฌ'
12 'ญ'
13 'ฎ'
14 'ฏ'
15 'ฐ'
16 'ฑ'
17 'ฒ'
18 'ณ'
19 'ด'
20 'ต'
21 'ถ'
22 'ท'
23 'ธ'
24 'น'
25 'บ'
26 'ป'
27 'ผ'
28 'ฝ'
29 'พ'
30 'ฟ'
31 'ภ'
32 'ม'
33 'ย'
34 'ร'
35 'ล'
36 'ว'
37 'ศ'
38 'ษ'
39 'ส'
40 'ห'
41 'ฬ'
42 'อ'
43 'ฮ'
44 ‘ฤ’
45 ‘ฤา’
46 ‘ฦ’
47 ‘ฦา’
48 ‘ะ’
49 'ั'
50 'า'
51 'ำ'
52 'ิ'
53 'ี'
54 'ึ'
55’ื’
56 'ุ'
57 'ู'
58 'เ'
59 '็'
60 'โ'
61 ’์’
62 ’แ’
63 ’ใ’
64 ’ไ’
