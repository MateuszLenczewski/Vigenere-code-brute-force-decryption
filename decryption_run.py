zawartosc = open("dictionary.txt").read()
def dict(word):
    if word in zawartosc:
        return True
    else:
        return False

def check_if_in_english(text, accuracy):
    text = text.lower()
    text = text.split(" ")
    special_signs = [",",".","!","?",":",";","\"","\'","(",")","$"]
    text_copy = []
    words_in_dict = 0
    total_words = 0
    for word in text:
        for sign in special_signs:
            if sign in word:
                word = word.replace(sign,"")
        total_words += 1
        if dict(word):
            words_in_dict += 1
    percentage = words_in_dict/total_words
    if percentage*100>=accuracy:
        return True
    return False

def key_generator(length):
    import itertools
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    keywords = []
    keywords = [''.join(k) for k in itertools.product(alphabets, repeat = length)]
    return keywords

def dec_vigenere(tekst, klucz):
    tekst = tekst.upper()
    klucz = klucz.upper()
    wynik = ""
    i = 0
    for x in tekst:
        if i>len(klucz)-1:
            i = 0
        if ord(x) > 64 and ord(x) < 91:
            if (ord(x) - ord(klucz[i]))+65 < 65:
                wynik += chr(ord(x) - ord(klucz[i]) + 26+66)
            else:
                wynik += chr(ord(x) - ord(klucz[i])+65)
        else:
            wynik += x
            i -=1
        i += 1
    return wynik.lower()


def decode_vigenere(tekst):
    for y in range(1,6):
        keys = key_generator(y)
        for key in keys:
            if check_if_in_english(dec_vigenere(tekst,key),60):
                print(key + ", " + dec_vigenere(tekst, key))


print(decode_vigenere(text))
