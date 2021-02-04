
def fahreinheit_to_celsius(temp):
    celsius = (temp - 32)*5/9
    return celsius


def celsius_to_fahrenheit(num):
    fahren = num*(9/5) + 32
    return fahren

tmp_fah = fahreinheit_to_celsius(50)
print(tmp_fah)
tmp_cel = celsius_to_fahrenheit(50)
print(tmp_cel)