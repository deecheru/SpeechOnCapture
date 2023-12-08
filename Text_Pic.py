import easyocr


def extract_text_from_image(image_path, language='en'):
    try:
        # Create an OCR reader using easyocr
        reader = easyocr.Reader([language])

        # Read text from the image
        result = reader.readtext(image_path)

        # Extract and return the text
        text = ' '.join([entry[1] for entry in result])
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
