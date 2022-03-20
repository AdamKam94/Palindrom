

def WordLen(Word):      
    Word = Word.lower()
    if len(Word) % 2 == 0:        
        HalfLen = int(len(Word)/2)
        WordPrefix = Word[0:HalfLen]
        WordSuffix = Word[HalfLen:][::-1]
        if WordPrefix == WordSuffix:
            print("Wyraz ",Word," to palindrom")
        else:
            print("Wyraz ",Word," nie jest palindromem")
        
    else: 
        HalfLen = int(len(Word)/2)
        WordPrefix = Word[0:HalfLen]
        WordSuffix = Word[HalfLen+1:][::-1]
        if WordPrefix == WordSuffix:
            print("Wyraz ",Word," to palindrom")
        else:
            print("Wyraz ",Word," nie jest palindromem")

    #fdsc
    


    


