# Text Summarizer

A Python-based text summarization tool that uses Google's Gemini AI API to generate concise, coherent summaries from long text documents.

## Features

- 🤖 **AI-Powered Summarization**: Uses Google's Gemini 2.5 Flash model for high-quality summaries
- 📁 **File-Based Input/Output**: Reads from text files and saves summaries to output files
- 🔧 **Configurable System Prompts**: Customizable summarization behavior via external prompt files
- 🛡️ **Secure API Key Management**: Uses environment variables for secure credential storage
- 📝 **Comprehensive Logging**: Detailed logging with timestamps for debugging and monitoring
- ⚙️ **Command Line Interface**: Easy-to-use CLI with configurable model selection
- 🚀 **Production Ready**: Robust error handling and professional code structure

## Prerequisites

- Python 3.11 or higher
- Google Gemini API key
- Required Python packages (see Installation)

## Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd summarize
   ```

2. **Install required Python packages**
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. **Set up your API key**
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## Project Structure

```
summarize/
├── src/
│   └── main.py              # Main application script
├── data/
│   ├── input.txt            # Input text file to summarize
│   ├── output.txt           # Generated summary (created automatically)
│   └── system_prompt.txt    # Custom system prompt for summarization
├── .env                     # Environment variables (create this file)
├── .env.example             # Template for environment variables
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Usage

### Basic Usage

1. **Prepare your input text**
   - Place the text you want to summarize in `data/input.txt`

2. **Run the summarizer**
   ```bash
   python src/main.py
   ```

3. **Check the results**
   - The summary will be saved to `data/output.txt`
   - Check the console for logging information

### Advanced Usage

**Using a different model:**
```bash
python src/main.py --model gemini-1.5-pro
```

**Available models:**
- `gemini-2.5-flash` (default) - Fast and efficient
- `gemini-1.5-pro` - More powerful but slower
- `gemini-1.5-flash` - Balanced performance

## Configuration

### Customizing the System Prompt

Edit `data/system_prompt.txt` to customize how the AI summarizes text. The default prompt is designed for general summarization, but you can modify it for specific use cases.

Example custom prompt:
```
You are a technical writer. Summarize the given text focusing on key technical concepts, 
maintaining accuracy while making it accessible to a general audience.
```

### Environment Variables

Create a `.env` file with:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## API Key Setup

1. **Get a Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key

2. **Add to your environment**
   - Copy the key to your `.env` file
   - Never commit your actual API key to version control

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- File not found errors
- Empty input files
- API request failures
- File writing errors

All errors are logged with timestamps for easy debugging.

## Logging

The application uses Python's logging module with the following features:
- **INFO level**: Successful operations and summary generation
- **ERROR level**: File errors, API failures, and missing configurations
- **Timestamped entries**: All log entries include timestamps
- **Structured format**: Consistent log message format

## Development

### Code Structure

- **Modular Design**: Functions are separated by responsibility
- **Type Hints**: All functions include type annotations
- **Docstrings**: Comprehensive documentation for all functions
- **Error Handling**: Robust exception handling throughout

### Key Functions

- `get_input_text()`: Reads and validates input file
- `write_output_file()`: Saves summary to output file
- `get_system_prompt()`: Loads custom system prompt
- `run_summarizer()`: Main summarization logic
- `read_file_safely()`: Helper for safe file operations

## Troubleshooting

### Common Issues

**"Gemini API key not found"**
- Ensure your `.env` file exists and contains `GEMINI_API_KEY=your_key`
- Check that the key is valid and has proper permissions

**"File not found"**
- Verify that `data/input.txt` exists
- Check that `data/system_prompt.txt` exists

**"No summary generated"**
- Check your internet connection
- Verify your API key is valid
- Ensure your input text is not empty

### Debug Mode

For additional debugging information, you can modify the logging level in `main.py`:
```python
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:
- Check the troubleshooting section above
- Review the logging output for error details
- Ensure all prerequisites are met

---

**Happy Summarizing! 📚✨**