def get_maximum_value(a,b,c):
    
    max = a
    if b > max:
        max = b
        if c > max:
            max = c
    elif c > max:
        max = c
    return max

max_val = get_maximum_value(0,0,1)
print(max_val)