array = ["ab","a","para"]
word = "a"

def countOccurrences(array, word):
    lista = str(array)
    wordslist = lista.count(word)
    large = len(array)
    return wordslist, large

print(countOccurrences(array, word))
