from langdetect import detect
# vhelper.py>

# functions
def check_if_english(string):
    try:
        language = detect(string)
        return language == "en"
    except:
        return False

def stretch_key(string, key):
    key = list(key)
    stretched_key = []
    i = 0
    for char in string:
        if char == " ":
            stretched_key.append(" ")
        else:
            stretched_key.append(key[i % len(key)])
            i += 1
    return "" . join(stretched_key)