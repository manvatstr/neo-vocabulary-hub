# Polish → Ukrainian Vocabulary Generation Prompt

```
Generate {WORDS_PER_CHUNK} common B1-level vocabulary words related to the theme '{category}' (specifically focusing on: '{subcategory}').
The words should be translated from Polish to Ukrainian.

Output format MUST be strictly CSV with no headers, no markdown blocks, no numbering, and separated by semicolons (;).
Format: foreign_word;ukrainian_word;polish_plural;category_tag;lemma;lemma_translation;part_of_speech;reserved

## CARD DISPLAY STRUCTURE (top to bottom):
1. Polish word (the word being learned — column 1)
2. Polish plural form (grammatical feature — column 3)
3. Ukrainian word (native translation — column 2)
4. Lemma family (columns 5 + 6)

## COLUMN RULES:
1. 'foreign_word': The word in Polish (must include proper diacritics: ą, ć, ę, ł, ń, ó, ś, ź, ż)
2. 'ukrainian_word': The word in Ukrainian (must use proper Ukrainian diacritics)
3. 'polish_plural': The plural form in Polish (with proper diacritics), if countable noun, otherwise empty
4. 'category_tag': Always '{category}' (do not substitute)
5. 'lemma': The root dictionary form (lemma) of the foreign_word in nominative singular case. If already a lemma, repeat it.
6. 'lemma_translation': The translation of the lemma in Ukrainian
7. 'part_of_speech': The part of speech using standardized terms (see below)
8. 'reserved': Leave this column EMPTY. Polish orthography is largely transparent for Ukrainian speakers, so no transliteration is needed.

## CRITICAL RULES FOR POLISH:
- Always include proper diacritics (ą, ć, ę, ł, ń, ó, ś, ź, ż)
- For nouns: lemma must be in nominative singular case
- For verbs: specify aspect (perfective/imperfective) in part_of_speech (e.g., 'verb (imperfective)')
- For adjectives: provide masculine singular form as lemma
- For plural forms: include only Polish plural (no Ukrainian words)

## STANDARDIZED PART OF SPEECH TERMS:
- noun
- verb (imperfective)
- verb (perfective)
- adj
- adv
- prep (preposition)
- conj (conjunction)
- pron (pronoun)
- num (numeral)
- interj (interjection)

## QUALITY ASSURANCE RULES:
- Verify lemma and foreign_word are different when the word is inflected
- Ensure lemma_translation matches the lemma's meaning
- Cross-check that plural forms are only provided for countable nouns
- Never include explanatory text, notes, or example sentences
- Avoid hyphenation or line breaks within words
- Ensure all semicolons are followed by content (no trailing semicolons except column 8 which is empty)

## CULTURAL CONTEXT NOTES:
- Prioritize words used in everyday conversation
- Include terms relevant to both formal and informal contexts
- Prefer variants common in both Polish and Ukrainian cultures
- Avoid culturally sensitive terms unless essential for B1 level

## VALIDATION EXAMPLES (must match these patterns exactly):
# Nouns (with plural)
jabłko;яблуко;jabłka;{category};jabłko;яблуко;noun;
dziecko;дитина;dzieci;{category};dziecko;дитина;noun;
woda;вода;;{category};woda;вода;noun;

# Verbs (specify aspect)
czytać;читати;;{category};czytać;читати;verb (imperfective);
przeczytać;прочитати;;{category};przeczytać;прочитати;verb (perfective);

# Adjectives
zielony;зелений;;{category};zielony;зелений;adj;

# Other parts of speech
często;часто;;{category};często;часто;adv;
w;в;;{category};w;в;prep;

## ERROR PREVENTION:
- Never use quotation marks around words
- Do not include example sentences or usage notes
- Ensure proper diacritics in both Polish and Ukrainian words
- Verify verb aspect is correctly specified
- Confirm plural forms follow Polish grammar rules
- Column 8 must always be EMPTY

Ensure output contains ONLY the requested words, formatted strictly as specified above.