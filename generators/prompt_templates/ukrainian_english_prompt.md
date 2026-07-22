# Ukrainian → English Vocabulary Generation Prompt

```
Generate {WORDS_PER_CHUNK} common B1-level vocabulary words related to the theme '{category}' (specifically focusing on: '{subcategory}').
The words should be translated from Ukrainian to English.

Output format MUST be strictly CSV with no headers, no markdown blocks, no numbering, and separated by semicolons (;).
Format: foreign_word;ukrainian_word;transliteration_and_gender;category_tag;lemma;lemma_translation;part_of_speech;reserved

## CARD DISPLAY STRUCTURE (top to bottom):
1. Ukrainian word (the word being learned — column 2)
2. Latin transliteration + gender (pronunciation guide for English speakers — column 3)
3. English word (native translation — column 1)
4. Lemma family (columns 5 + 6)

## COLUMN RULES:
1. 'foreign_word': The word in English (do not capitalize unless proper noun)
2. 'ukrainian_word': The word in Ukrainian (must use proper Ukrainian diacritics: ї, є, ґ, etc.)
3. 'transliteration_and_gender': Latin-script transliteration of the UKRAINIAN word, approximating Ukrainian pronunciation for English speakers. For nouns, append a slash and gender abbreviation: m. (masculine), f. (feminine), n. (neuter). For uncountable nouns add: unc. For non-nouns (verbs, adjectives, adverbs, etc.) — transliteration only, no gender.
4. 'category_tag': Always '{category}' (do not substitute)
5. 'lemma': The root dictionary form of the foreign_word. If already a lemma, repeat it.
6. 'lemma_translation': The translation of the lemma in Ukrainian (for verbs, specify aspect: e.g., 'писати (imperfective)')
7. 'part_of_speech': The part of speech using standardized terms (see below)
8. 'reserved': Leave this column EMPTY

## TRANSLITERATION RULES:
- Use simplified Latin-script transliteration that an English speaker can read aloud to approximate the Ukrainian pronunciation
- Use common romanization: я→ya, є→ye, ї→yi, ю→yu, ж→zh, ч→ch, ш→sh, щ→shch, ц→ts, х→kh, г→h, ґ→g, ь→(soften preceding consonant or omit)
- Examples: яблуко→yabluko, вода→voda, читати→chytaty, щастя→shchastya, місто→misto

## CRITICAL RULES FOR UKRAINIAN:
- Lemma must be in nominative singular case for nouns
- For nouns: gender is embedded in column 3 after slash (m./f./n./unc.)
- For verbs: specify aspect (perfective/imperfective) in lemma_translation
- For adjectives: provide masculine singular form as lemma
- Use proper Ukrainian diacritics (ї, є, ґ, etc.)

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
- Cross-check that gender abbreviation matches the Ukrainian noun's actual grammatical gender
- Never include explanatory text, notes, or example sentences
- Avoid hyphenation or line breaks within words
- Ensure all semicolons are followed by content (no trailing semicolons except column 8 which is empty)

## CULTURAL CONTEXT NOTES:
- Prioritize words used in everyday conversation in both languages
- Include terms relevant to both formal and informal contexts
- For culturally specific terms, provide the most widely understood translation
- Avoid idioms or expressions that don't translate literally

## VALIDATION EXAMPLES (must match these patterns exactly):
# Nouns (transliteration + gender)
apple;яблуко;yabluko / n.;{category};apple;яблуко;noun;
water;вода;voda / f.;{category};water;вода;noun;
table;стіл;stil / m.;{category};table;стіл;noun;

# Verbs (transliteration only, no gender)
write;писати;pysaty;{category};write;писати (imperfective);verb;
read;читати;chytaty;{category};read;читати (imperfective);verb;

# Adjectives (transliteration only)
red;червоний;chervonyi;{category};red;червоний;adj;

# Adverbs
often;часто;chasto;{category};often;часто;adv;

## ERROR PREVENTION:
- Never use quotation marks around words
- Do not capitalize English words unless proper nouns
- Ensure transliteration uses LATIN characters (NOT Cyrillic)
- Gender abbreviation must be one of: m. / f. / n. / unc.
- Verify Ukrainian diacritics are used correctly
- Confirm verb aspect is specified in lemma_translation
- Column 8 must always be EMPTY

Ensure output contains ONLY the requested words, formatted strictly as specified above.