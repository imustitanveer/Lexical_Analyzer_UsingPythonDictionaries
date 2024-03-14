# Lexical Analyzer Using Python Dictionaries

This is a simple lexical analyzer implemented in Python that uses dictionaries to create tokens from input strings.

## Features

- Tokenizes input strings based on specified rules.
- Uses Python dictionaries for efficient tokenization.
- Easy to customize for different languages or tokenization requirements.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/imustitanveer/Lexical_Analyzer_UsingPythonDictionaries.git
   ```

2. Run the `lexical_analyzer.py` file:

   ```bash
   python lexical_analyzer.py
   ```

3. Enter an input string when prompted, and the analyzer will generate tokens based on the specified rules.

## Examples

For example, if the input string is:

```text
int x = 10;
```

The analyzer might generate the following tokens:

- `int`: Keyword
- `x`: Identifier
- `=`: Assignment Operator
- `10`: Integer Constant
- `;`: Semicolon

## Customization

You can customize the rules for tokenization by modifying the dictionaries in the `lexical_analyzer.py` file. For example, you can add new keywords, operators, or constants based on your requirements.
