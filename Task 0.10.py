def common_characters(string_a,string_b):
    
    lis = []
    for i in string_b:
        for j in string_a:
            if j == i:
                lis.append(j)

    unique_lis = []
    for word in lis:
        if word not in unique_lis:
            unique_lis.append(word)

    
    print("Common Letters: " + ', '.join(unique_lis))
    
