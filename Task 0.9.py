def get_vowels(string):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    lis = []
    for i in string:
        for j in vowels:
            if j == i:
                lis.append(j)
    print(', '.join(lis))

get_vowels("lolOabanEilwU")