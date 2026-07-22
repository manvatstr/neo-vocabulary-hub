# Vocabulary Generation Prompt Templates

This directory contains language-specific prompt templates for generating B1-level vocabulary lists.

## Card Display Structure

All templates follow a unified card display structure (top to bottom):

1. **Word** — the word in the language being learned (first in pair)
2. **Feature / Pronunciation** — either a grammatical feature of the learning language, OR a transliterative transcription in the native language, OR both
3. **Translation** — the word translated into the native language (second in pair)
4. **Family** — lemma and its translation

## Per-Pair Feature Line (Line 2)

| Pair | Line 2 Content | Column | Rationale |
|------|---------------|--------|-----------|
| **uk_en** | Latin transliteration + gender (`yabluko / n.`) | col 3 | English speakers need pronunciation guide for Cyrillic; Ukrainian has grammatical gender |
| **de_uk** | German plural (`die Äpfel`) | col 3 | Plurals are the key learning challenge in German |
| **pl_uk** | Polish plural (`jabłka`) | col 3 | Polish orthography is largely transparent for Ukrainian speakers |
| **es_uk** | Spanish plural (`los libros`) | col 3 | Plurals with articles are key feature of Spanish |

### Transliteration (Column 8)

| Pair | Transliteration | Script | Rationale |
|------|----------------|--------|-----------|
| **uk_en** | *(merged into col 3)* | Latin | Combined with gender in col 3 |
| **de_uk** | `апфель`, `вассер` | Cyrillic | German pronunciation is non-trivial for Ukrainian speakers |
| **pl_uk** | *(empty)* | — | Polish is phonetically close to Ukrainian |
| **es_uk** | `лібро`, `абляр` | Cyrillic | Spanish phonetics differ significantly from Ukrainian |

## CSV Format

All templates produce 8-column semicolon-separated CSV:

```
col1;col2;col3;col4;col5;col6;col7;col8
```

| Column | Name | Content |
|--------|------|---------|
| 1 | foreign_word | Word in the learning language (with articles where applicable) |
| 2 | native_word | Translation in the native language |
| 3 | feature | Plural, transliteration+gender, or other grammatical feature |
| 4 | category_tag | Category identifier |
| 5 | lemma | Root dictionary form |
| 6 | lemma_translation | Translation of the lemma |
| 7 | part_of_speech | Standardized POS tag |
| 8 | transliteration | Cyrillic pronunciation guide (or empty) |

## Usage

```python
with open(f"prompt_templates/{template_name}.md", "r") as f:
    prompt_template = f.read()

prompt = prompt_template.format(
    WORDS_PER_CHUNK=WORDS_PER_CHUNK,
    category=category,
    subcategory=subcategory
)
```