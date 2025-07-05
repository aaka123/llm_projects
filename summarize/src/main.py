import os
import logging
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_path_of_file(file_name: str) -> str:
    """Returns the full path to a file in the data directory."""
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "..", "data", file_name)
    return path

def read_file_safely(file_path: str, error_context: str) -> str:
    """Reads a file safely with comprehensive error handling."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        exit(1)
    except Exception as e:
        logging.error(f"Error reading {error_context}: {e}")
        exit(1)
    if not content.strip():
        logging.error(f"{error_context} is empty")
        exit(1)
    return content

def get_input_text() -> str:
    """Reads and returns the content of the input file."""
    input_path = get_path_of_file("input.txt")
    return read_file_safely(input_path, "input file")

def write_output_file(response_text: str) -> None:
    """Writes the response text to the output file."""
    output_path = get_path_of_file("output.txt")
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(response_text)
        logging.info(f"Summary written to {output_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {output_path}")
        exit(1)
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        exit(1)

def get_system_prompt() -> str:
    """Reads and returns the system prompt from file."""
    path = get_path_of_file("system_prompt.txt")
    return read_file_safely(path, "system prompt file")

def run_summarizer(gemini_api_key: str, model_name: str) -> None:
    """Runs the summarization process using the specified model and API key."""
    genai.configure(api_key=gemini_api_key)
    system_prompt = get_system_prompt()
    model = genai.GenerativeModel(model_name, system_instruction=system_prompt)
    article = get_input_text()
    response = model.generate_content(article)
    if response.text:
        write_output_file(response.text)
    else:
        logging.error("No summary generated")
        exit(1)

def get_keys(model: str) -> str:
    """Gets the API key for the specified model."""
    key_name = get_key_name(model)
    return os.getenv(key_name)

def get_key_name(model: str) -> str:
    """Returns the environment variable name for the specified model's API key."""
    if "gemini" in model:
        return "GEMINI_API_KEY"
    return ""

def parse_argument():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Summarize a text file using Gemini API")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash", help="Model name")
    return parser.parse_args()

if __name__ == "__main__":
    load_dotenv()
    args = parse_argument()
    gemini_api_key = get_keys(args.model)
    if not gemini_api_key:
        logging.error("Gemini API key not found. Please set it in your .env file")
        exit(1)
    run_summarizer(gemini_api_key, args.model)