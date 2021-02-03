def get_maximum_value(a,b,c):
    max = a
    if b > max:
        max = b
    elif c > max:
        max = c
    return max
max_val = get_maximum_value(12,45,8)
print(max_val)