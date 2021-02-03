# function to convert fahreinheit to celsius
def fahreinheit_tocelsius(temp):
    celsius = (temp - 32)*5/9
    return celsius

# function to convert celsisu to fahreinheit
def celsius_tofahrenheit(num):
    fahren = num*(9/5) + 32
    return fahren

tmp_fah = fahreinheit_tocelsius(50)
print(tmp_fah)
tmp_cel = celsius_tofahrenheit(50)
print(tmp_cel)