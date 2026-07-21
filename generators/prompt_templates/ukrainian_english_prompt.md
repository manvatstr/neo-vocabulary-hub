# Ukrainian → English Vocabulary Generation Prompt

```
Generate {WORDS_PER_CHUNK} common B1-level vocabulary words related to the theme '{category}' (specifically focusing on: '{subcategory}').
The words should be translated from Ukrainian to English.

Output format MUST be strictly CSV with no headers, no markdown blocks, no numbering, and separated by semicolons (;).
Format: foreign_word;ukrainian_word;english_plural_and_gender;category_tag;lemma;lemma_translation;part_of_speech;transliteration

## COLUMN RULES:
1. 'foreign_word': The word in English (do not capitalize unless proper noun)
2. 'ukrainian_word': The word in Ukrainian (must use proper Ukrainian diacritics: ї, є, ґ, etc.)
3. 'english_plural_and_gender': The plural form in English if countable noun, otherwise empty. For Ukrainian nouns, add grammatical gender in parentheses (e.g., 'tables (neuter)', 'water (uncountable)')
4. 'category_tag': Always '{category}' (do not substitute)
5. 'lemma': The root dictionary form of the foreign_word. If already a lemma, repeat it.
6. 'lemma_translation': The translation of the lemma in Ukrainian (for verbs, specify aspect: e.g., 'писати (imperfective)')
7. 'part_of_speech': The part of speech using standardized terms (see below)
8. 'transliteration': Ukrainian transliterative pronunciation guide (e.g., 'епл' for 'apple', 'вота' for 'water')

## CRITICAL RULES FOR UKRAINIAN:
- Lemma must be in nominative singular case for nouns
- For nouns: specify grammatical gender (masculine/feminine/neuter) in plural_and_gender column
- For verbs: specify aspect (perfective/imperfective) in lemma_translation
- For adjectives: provide masculine singular form as lemma
- Use proper Ukrainian diacritics (ї, є, ґ, etc.)
- For uncountable nouns: note 'uncountable' in gender field

## STANDARDIZED PART OF SPEECH TERMS:
- noun
- verb
- adj
- adv
- prep (preposition)
- conj (conjunction)
- pron (pronoun)
- num (numeral)
- interj (interjection)

## QUALITY ASSURANCE RULES:
- Verify lemma and foreign_word are different when the word is inflected
- Ensure lemma_translation includes aspect for verbs
- Cross-check that plural forms match the noun's countability
- Never include explanatory text, notes, or example sentences
- Avoid hyphenation or line breaks within words
- Ensure all semicolons are followed by content (no trailing semicolons)

## CULTURAL CONTEXT NOTES:
- Prioritize words used in everyday conversation in both languages
- Include terms relevant to both formal and informal contexts
- For culturally specific terms, provide the most widely understood translation
- Avoid idioms or expressions that don't translate literally

## VALIDATION EXAMPLES (must match these patterns exactly):
# Nouns (with gender specification)
apple;яблуко;apples (neuter);{category};apple;яблуко;noun;епл
water;вода;water (uncountable);{category};water;вода;noun;вота

# Verbs (with aspect)
write;писати;;{category};write;писати (imperfective);verb;райт
read;читати;;{category};read;читати (imperfective);verb;рід

# Adjectives
red;червоний;;{category};red;червоний;adj;ред

# Ukrainian case forms
стіл;table;tables (masculine);{category};стіл;table;noun;тейбл

## ERROR PREVENTION:
- Never use quotation marks around words
- Do not capitalize English words unless proper nouns
- Ensure transliterative transcription uses Cyrillic characters to approximate English pronunciation
- Verify Ukrainian diacritics are used correctly
- Confirm verb aspect is specified in lemma_translation
- Check that gender specification matches Ukrainian grammar

Ensure output contains ONLY the requested words, formatted strictly as specified above.