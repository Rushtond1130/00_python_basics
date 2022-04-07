# ask the user for their name
username = input ("what is your name? ")

# ask the user for their favourite integer
fav_num = int(input("Favourite Number"))

# double, half and square the number
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

# Greet the user
print("Hello {}, your favourite number is {}.".format(username,fav_num))
print()
# output the results of doubling, halfing 
# and squaring their faovurite number
print("double {} is {}.".format(fav_num, double))
print("half {} is {}.".format(fav_num, half))
print("{} squared is {}.".format(fav_num, square))
print()