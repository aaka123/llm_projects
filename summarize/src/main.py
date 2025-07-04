import os
import logging
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_path_of_file(file_name):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir,"..","data",file_name)
    return path

def get_input_text():
    input_path = get_path_of_file("input.txt")
    try:
        with open(input_path, "r",encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {input_path}")
        exit(1)
    except Exception as e:
        logging.error(f"Error reading file:{e}")
        exit(1)
    if not article.strip():
        logging.error("Input file is empty")
        exit(1)
    return article

def write_output_file(response_text):
    output_path = get_path_of_file("output.txt")
    try:
        with open(output_path, "w",encoding="utf-8") as file:
            file.write(response_text)
        logging.info(f"Summary written to {output_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {output_path}")
        exit(1)
    except Exception as e:
        logging.error(f"Error writing to file: {e}")

def get_system_prompt():
    path = get_path_of_file("system_prompt.txt")
    try:
        with open(path, "r",encoding="utf-8") as file:
            system_prompt = file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {path}")
        exit(1)
    except Exception as e:
        logging.error(f"Error reading file:{e}")
        exit(1)
    if not system_prompt.strip():
        logging.error("Input file is empty")
        exit(1)
    return system_prompt

def run_summarizer(gemini_api_key,model_name):
    genai.configure(api_key = gemini_api_key)
    system_prompt =  get_system_prompt()
    model = genai.GenerativeModel(model_name,system_instruction = system_prompt) 
    article = get_input_text()
    response = model.generate_content(article)
    if response.text :
        write_output_file(response.text)
    else:
        logging.error("No summary generated")
        exit(1)

def get_keys(model):
    key_name = get_key_name(model)
    return os.getenv(key_name)

def get_key_name(model):
    if "gemini" in model:
        return "GEMINI_API_KEY"

def parse_argument():
    parser = argparse.ArgumentParser(description="Summarize a text file using Gemini API")
    parser.add_argument("--model",type=str,default="gemini-2.5-flash",help="Model_name")
    return parser.parse_args()

if __name__ == "__main__":
    load_dotenv()
    args = parse_argument()
    gemini_api_key = get_keys(args.model)
    if not gemini_api_key:
        logging.error("Gemini API key not found. Please set it in your .env file")
        exit(1)
    run_summarizer(gemini_api_key,args.model)