# German → Ukrainian Vocabulary Generation Prompt

```
Generate {WORDS_PER_CHUNK} common B1-level vocabulary words related to the theme '{category}' (specifically focusing on: '{subcategory}').
The words should be translated from German to Ukrainian.

Output format MUST be strictly CSV with no headers, no markdown blocks, no numbering, and separated by semicolons (;).
Format: foreign_word;ukrainian_word;german_plural;category_tag;lemma;lemma_translation;part_of_speech;transliteration

## COLUMN RULES:
1. 'foreign_word': The word in German (include definite article: der/die/das for nouns)
2. 'ukrainian_word': The word in Ukrainian (must use proper Ukrainian diacritics)
3. 'german_plural': The plural form in German (with article 'die'), if countable noun, otherwise empty
4. 'category_tag': Always '{category}' (do not substitute)
5. 'lemma': The root dictionary form of the foreign_word. For compounds, include components (e.g., 'Wasser + Fall')
6. 'lemma_translation': The translation of the lemma in Ukrainian
7. 'part_of_speech': The part of speech using standardized terms (see below)
8. 'transliteration': Ukrainian transliterative pronunciation guide (e.g., 'апфель' for 'Apfel', 'васса' for 'Wasser')

## CRITICAL RULES FOR GERMAN:
- Always include definite articles (der/die/das) for nouns
- For compound nouns: provide components in lemma field
- For verbs: specify type (weak/strong/mixed/separable) in part_of_speech
- For plurals: include umlaut changes where applicable
- For adjectives: provide base form (without endings)
- For separable verbs: include full form with 'zu' in lemma

## STANDARDIZED PART OF SPEECH TERMS:
- noun
- verb (weak)
- verb (strong)
- verb (mixed)
- verb (separable)
- adj
- adv
- prep (preposition)
- conj (conjunction)
- pron (pronoun)
- num (numeral)
- interj (interjection)

## QUALITY ASSURANCE RULES:
- Verify article (der/die/das) matches the noun's grammatical gender
- Ensure lemma includes components for compound nouns
- Cross-check that plural forms follow German grammar rules (including umlauts)
- Never include explanatory text, notes, or example sentences
- Avoid hyphenation or line breaks within words
- Ensure all semicolons are followed by content (no trailing semicolons)

## CULTURAL CONTEXT NOTES:
- Prioritize words used in everyday conversation in German-speaking countries
- Include terms relevant to both formal and informal contexts
- For region-specific terms (Austria/Switzerland), prefer standard German variants
- Avoid culturally sensitive terms unless essential for B1 level

## VALIDATION EXAMPLES (must match these patterns exactly):
# Nouns (regular and irregular plurals)
der Apfel;яблуко;die Äpfel;{category};Apfel;яблуко;noun;апфель
der Vater;батько;die Väter;{category};Vater;батько;noun;фата

# Compound nouns
der Wasserfall;водоспад;;{category};Wasser + Fall;водоспад;noun;вассефаль

# Verbs (specify type)
lesen;читати;;{category};lesen;читати;verb (strong);лєзен
einkaufen;купувати;;{category};einkaufen (zu kaufen);купувати;verb (separable);айнкауфен

# Adjectives
kalt;холодний;;{category};kalt;холодний;adj;кальт

# Umlaut plurals
der Bruder;брат;die Brüder;{category};Bruder;брат;noun;бруда

## ERROR PREVENTION:
- Never use quotation marks around words
- Do not include example sentences or usage notes
- Ensure articles match the noun's grammatical gender
- Verify verb types are correctly specified
- Confirm plural forms include umlaut changes where applicable
- Check that separable verbs include 'zu' form in lemma

Ensure output contains ONLY the requested words, formatted strictly as specified above.