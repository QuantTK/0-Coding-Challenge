def common_characters(string_a,string_b):
    
    lis = []
    for i in string_a:
        for j in string_b:
            if j == i:
                lis.append(j)
                
    print("Common Letters:" + ', '.join(lis))
    
common_characters("House","computers")