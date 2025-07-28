from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
import os, json

def parse_pdf(file_path):
    headings = []
    title = None
    font_sizes = {}

    for page_num, page_layout in enumerate(extract_pages(file_path), start=1):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    font_size = 0
                    text = text_line.get_text().strip()
                    for char in text_line:
                        if isinstance(char, LTChar):
                            font_size = max(font_size, char.size)
                    if not text: continue
                    
                    # Capture font sizes
                    font_sizes[text] = font_size
                    
                    # Title detection
                    if page_num == 1 and (title is None or font_size > font_sizes.get(title, 0)):
                        title = text
                    
                    # Heading detection by font size thresholds (refine later)
                    if font_size >= 16:
                        level = "H1"
                    elif 14 <= font_size < 16:
                        level = "H2"
                    elif 12 <= font_size < 14:
                        level = "H3"
                    else:
                        continue
                    
                    headings.append({
                        "level": level,
                        "text": text,
                        "page": page_num
                    })

    return {
        "title": title,
        "outline": headings
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            result = parse_pdf(os.path.join(input_dir, filename))
            json_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(json_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
