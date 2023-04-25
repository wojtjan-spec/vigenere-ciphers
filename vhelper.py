# vhelper.py>

# function
def stretch_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            if (string[i] == " "):
                key.append(" ")
            else:
                key.append(key[i % len(key)])
    return("" . join(key))