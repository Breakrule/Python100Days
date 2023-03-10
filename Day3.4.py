height = int(input("input your height : "))
price = int(0)

if height >= 120:
    print("You can ride")
    age = int(input("input your age : "))
    if age < 12:
        price = 5
        print("Child tickets are $5.")
    elif age <= 18:
        price = 7
        print("Youth tickets are $7.")
    else:
        price = 12
        print("Adult tickets are $12.")
    add_photo = input("Do you want to add a photo ? Y or N. ")
    if add_photo == "Y" or add_photo == "y":
        price += 3

    print(f"The total bill is ${price}")

else:
    print("Sorry, you have to grow taller before you can ride.")