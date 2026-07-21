# Vocabulary Generation Prompt Templates

This directory contains language-specific prompt templates for generating B1-level vocabulary lists. Each template is designed to:
- Ensure consistent CSV output format
- Handle language-specific grammatical features
- Produce high-quality, culturally appropriate vocabulary
- Prevent common errors in AI-generated content

## Template Structure

All templates follow this structure:
1. **Output Format Specification** - Strict CSV requirements
2. **Column Rules** - Detailed instructions for each field
3. **Language-Specific Rules** - Grammatical and orthographic requirements
4. **Standardized Part of Speech Terms** - Consistent terminology
5. **Quality Assurance Rules** - Validation requirements
6. **Cultural Context Notes** - Guidance for appropriate word selection
7. **Validation Examples** - Concrete examples of correct output
8. **Error Prevention** - Common pitfalls to avoid

## Language-Specific Templates

| Template | Key Features |
|----------|--------------|
| [polish_ukrainian_prompt.md](polish_ukrainian_prompt.md) | Polish diacritics, verb aspect, case declensions |
| [spanish_ukrainian_prompt.md](spanish_ukrainian_prompt.md) | Definite articles, verb conjugation groups, irregular plurals |
| [ukrainian_english_prompt.md](ukrainian_english_prompt.md) | Grammatical gender, verb aspect, IPA pronunciation |
| [german_ukrainian_prompt.md](german_ukrainian_prompt.md) | Compound nouns, verb types, umlaut plurals |

## Usage Guidelines

1. **Template Selection**: Use the appropriate template for each language pair
2. **Customization**: Replace `{WORDS_PER_CHUNK}`, `{category}`, and `{subcategory}` placeholders
3. **Validation**: Always verify output against the validation examples
4. **Quality Control**: Run generated content through the non-AI validation algorithms

## Integration with Generation Scripts

To use these templates in your generation scripts:

```python
# Example integration
with open(f"prompt_templates/{lang_source}_{lang_target}_prompt.md", "r") as f:
    prompt_template = f.read()

prompt = prompt_template.replace("{WORDS_PER_CHUNK}", str(WORDS_PER_CHUNK))
                       .replace("{category}", category)
                       .replace("{subcategory}", subcategory)
```

## Continuous Improvement

These templates should be regularly updated based on:
- User feedback from vocabulary reviews
- Common errors found in generated content
- Linguistic research on B1-level vocabulary
- Changes in language usage patterns