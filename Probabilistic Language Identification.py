from langdetect import detect

def detect_language_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            language = detect(text)
            return language
    except Exception as e:
        return f"Language detection failed: {str(e)}"

#main method
if __name__=="__main__":
    filename='letter.txt'
    detected_language = detect_language_from_file(filename)
    if detected_language:
        print(f"The detected language of the file is: {detected_language}")
    else:
        print("Failed to detect language.")