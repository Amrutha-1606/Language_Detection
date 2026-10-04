from langdetect import detect, LangDetectException

# Display project title
print("LANGUAGE DETECTION")
print("------------------")

# Get text from user
text = input("Enter some text: ")

# Check if input is empty
if not text.strip():
    print("Please enter some text.")
    exit()

try:
    # Detect language
    language_code = detect(text)

    # Language names
    languages = {
        "en": "English",
        "te": "Telugu",
        "hi": "Hindi",
        "ta": "Tamil",
        "kn": "Kannada",
        "ml": "Malayalam",
        "fr": "French",
        "es": "Spanish",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ar": "Arabic",
        "ru": "Russian",
        "ja": "Japanese",
        "ko": "Korean",
        "zh-cn": "Chinese"
    }

    # Get language name
    language_name = languages.get(
        language_code,
        "Unknown Language"
    )

    # Display result
    print("\nLanguage Code:", language_code)
    print("Detected Language:", language_name)

except LangDetectException:
    print("Unable to detect the language.")