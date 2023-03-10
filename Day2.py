# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

dead = int(90)
x_days = int(365) * dead
y_weeks = int(52) * dead
z_months = int(12) * dead

time_left = int(age)

days = x_days - (365 * time_left)
weeks = y_weeks - (52 * time_left)
months = z_months - (12 * time_left)

print("You have " + str(days) + " days, " + str(weeks) + " weeks, " + str(months) + " months left.")