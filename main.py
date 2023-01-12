import pytesseract
import re
from PIL import Image

ADDRESS_REGEX = r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b'
NAME_REGEX = r'\b[A-Z][a-z]+( [A-Z][a-z]+)*\b'
DOB_REGEX = r'\b(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d\b'
CONTACT_REGEX = r'\b(?:\+44|0) [0-9]{3} [0-9]{3} [0-9]{4}\b|\b(?:\+44|0) [0-9]{3} [0-9]{3} [0-9]{3}\b|\b(?:\+44|0) [' \
                r'0-9]{5} [0-9]{6}\b|\b(?:\+44|0) [0-9]{3} [0-9]{4} [0-9]{4}\b|\b(?:\+44|0) [0-9]{9}\b'
PHONE_REGEX = r'\b(?:(?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{' \
              r'3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4}))\b'
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# OCR function
def ocr_image(path):
    return pytesseract.image_to_string(Image.open(image_path))


def detect_info(text):
    """
     Regular expression patterns to match UK addresses, names, dates of birth, contact details, phone numbers and
     emails
    :param text:
    :return: None
    """

    # Find matches for each pattern
    address_matches = re.finditer(ADDRESS_REGEX, text)
    name_matches = re.finditer(NAME_REGEX, text)
    dob_matches = re.finditer(DOB_REGEX, text)
    contact_matches = re.finditer(CONTACT_REGEX, text)
    phone_matches = re.finditer(PHONE_REGEX, text)
    email_matches = re.finditer(EMAIL_REGEX, text)

    print("\n**** Addresses ****\n")
    for match in address_matches:
        print(match.group())
    print("\n**** Names ****\n")
    for match in name_matches:
        print(match.group())
    print("\n**** DOBs ****\n")
    for match in dob_matches:
        print(match.group())
    print("\n**** Contact details ****\n")
    for match in contact_matches:
        print(match.group())
    print("\n**** Phone numbers ****\n")
    for match in phone_matches:
        print(match.group())
    print("\n**** Emails ****\n")
    for match in email_matches:
        print(match.group())


image_path = "image.png"
text = ocr_image(image_path)
detect_info(text)
