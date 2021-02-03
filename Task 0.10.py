
def common_characters(string_a,string_b):
    # using nested loop to traverse trough the strings
    for i in string_a:
        for j in string_b:
            if j == i:
                print(j)
common_characters("House","computers") 