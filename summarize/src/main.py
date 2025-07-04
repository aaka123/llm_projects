import os
import logging
from transformers import pipeline

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_summarizer():
    summarizer = pipeline("summarization", model="t5-small")
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir,"..","data","input.txt")
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
    summary = summarizer(article, max_length=130, min_length=30, do_sample=True)
    if summary and 'summary_text' in summary[0]:
        logging.info(summary[0]['summary_text'])
    else:
        logging.error("No summary generated")
        exit(1)

if __name__ == "__main__":
    run_summarizer()