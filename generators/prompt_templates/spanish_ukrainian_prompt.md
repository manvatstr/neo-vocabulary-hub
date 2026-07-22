# Spanish → Ukrainian Vocabulary Generation Prompt

```
Generate {WORDS_PER_CHUNK} common B1-level vocabulary words related to the theme '{category}' (specifically focusing on: '{subcategory}').
The words should be translated from Spanish to Ukrainian.

Output format MUST be strictly CSV with no headers, no markdown blocks, no numbering, and separated by semicolons (;).
Format: foreign_word;ukrainian_word;spanish_plural;category_tag;lemma;lemma_translation;part_of_speech;transliteration

## CARD DISPLAY STRUCTURE (top to bottom):
1. Spanish word (the word being learned — column 1)
2. Spanish plural form (grammatical feature — column 3)
3. Ukrainian word (native translation — column 2)
4. Lemma family (columns 5 + 6)
Note: Column 8 (transliteration) provides Cyrillic pronunciation guide and may be displayed alongside the word.

## COLUMN RULES:
1. 'foreign_word': The word in Spanish (include definite article: el/la for nouns)
2. 'ukrainian_word': The word in Ukrainian (must use proper Ukrainian diacritics)
3. 'spanish_plural': The plural form in Spanish (with article 'los/las'), if countable noun, otherwise empty
4. 'category_tag': Always '{category}' (do not substitute)
5. 'lemma': The root dictionary form of the foreign_word. If already a lemma, repeat it.
6. 'lemma_translation': The translation of the lemma in Ukrainian
7. 'part_of_speech': The part of speech using standardized terms (see below)
8. 'transliteration': Ukrainian transliterative pronunciation guide using CYRILLIC characters to approximate Spanish pronunciation for Ukrainian speakers (e.g., 'лібро' for 'libro', 'абляр' for 'hablar')

## TRANSLITERATION RULES:
- Use Cyrillic characters that a Ukrainian speaker can read aloud to approximate Spanish pronunciation
- Common mappings: h→(silent), j→х, ll→й, ñ→нь, rr→рр, v→б/в, z→с (in Spain) or с, c(e/i)→с, g(e/i)→х, qu→к, gue/gui→ге/гі
- Examples: libro→лібро, hablar→абляр, comer→комер, vivir→вівір, rojo→рохо, lápiz→лапіс, manzana→мансана

## CRITICAL RULES FOR SPANISH:
- Always include definite articles (el/la) for nouns
- For verbs: specify conjugation group (-ar/-er/-ir) in part_of_speech (e.g., 'verb (-ar)')
- For adjectives: provide masculine singular form as lemma
- For irregular plurals: include the irregular form in plural column
- For heteronyms: provide separate entries for different meanings

## STANDARDIZED PART OF SPEECH TERMS:
- noun
- verb (-ar)
- verb (-er)
- verb (-ir)
- adj
- adv
- prep (preposition)
- conj (conjunction)
- pron (pronoun)
- num (numeral)
- interj (interjection)

## QUALITY ASSURANCE RULES:
- Verify lemma matches the base form of the foreign_word
- Ensure article (el/la) matches the noun's grammatical gender
- Cross-check that plural forms follow Spanish grammar rules
- Transliteration must use CYRILLIC characters (not Latin/IPA)
- Never include explanatory text, notes, or example sentences
- Avoid hyphenation or line breaks within words
- Ensure all semicolons are followed by content (no trailing semicolons)

## CULTURAL CONTEXT NOTES:
- Prioritize words used in everyday conversation in both Spain and Latin America
- Include terms relevant to both formal and informal contexts
- For geographically specific terms (foods, plants), prefer variants common in both cultures
- Avoid region-specific slang unless essential for B1 level

## VALIDATION EXAMPLES (must match these patterns exactly):
# Nouns (with plural and transliteration)
el libro;книга;los libros;{category};libro;книга;noun;лібро
la mano;рука;las manos;{category};mano;рука;noun;мано
el agua;вода;;{category};agua;вода;noun;агуа

# Verbs (specify conjugation group, transliteration)
hablar;говорити;;{category};hablar;говорити;verb (-ar);абляр
comer;їсти;;{category};comer;їсти;verb (-er);комер
vivir;жити;;{category};vivir;жити;verb (-ir);вівір

# Adjectives
rojo;червоний;;{category};rojo;червоний;adj;рохо
grande;великий;;{category};grande;великий;adj;гранде

# Irregular plurals
el lápiz;олівець;los lápices;{category};lápiz;олівець;noun;лапіс

## ERROR PREVENTION:
- Never use quotation marks around words
- Do not include example sentences or usage notes
- Ensure articles match the noun's grammatical gender
- Verify verb conjugation groups are correctly specified
- Confirm plural forms follow Spanish grammar rules (including irregulars)
- Transliteration must be Cyrillic (Ukrainian letters), NOT IPA or Latin

Ensure output contains ONLY the requested words, formatted strictly as specified above.