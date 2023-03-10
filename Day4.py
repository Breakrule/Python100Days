# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

import random as rd

random_side = rd.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")

