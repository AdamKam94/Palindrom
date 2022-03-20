
def WordLen(Word):
    global GlobalWord
    GlobalWord = Word
    global WordLenght
    WordLenght = len(Word)
    print("Długość wyroazu ", GlobalWord, "to ", WordLenght," litery.")
    if WordLenght % 2 == 0:        
        print("wyraz ", GlobalWord, "ma parzystą ilość liter")
        HalfLen = int(WordLenght/2)
        WordPrefix = GlobalWord[0:HalfLen]
        WordSuffix = (GlobalWord[HalfLen:])
        WordSuffix2 = WordSuffix[::-1]
        if WordPrefix == WordSuffix2:
            print("Wyraz ",GlobalWord," to palindrom")
        else:
            print("Wyraz ",GlobalWord," nie jest palindromem")
        
    else: 
        print("wyraz ",GlobalWord,"posiada nieparzystą liczbę liter")
        HalfLen = int(WordLenght/2)
        WordPrefix = GlobalWord[0:HalfLen]
        WordSuffix = (GlobalWord[HalfLen+1:])
        WordSuffix2 = WordSuffix[::-1]
        if str(WordPrefix) == str(WordSuffix2):
            print("Wyraz ",GlobalWord," to palindrom")
        else:
            print("Wyraz ",GlobalWord," nie jest palindromem")
    



WordLen("Kak")
