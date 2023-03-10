# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lower_1 = name1.lower()
lower_2 = name2.lower()

t1_letter = lower_1.count("t")
r1_letter = lower_1.count("r")
u1_letter = lower_1.count("u")
e1_letter = lower_1.count("e")
l1_letter = lower_1.count("l")
o1_letter = lower_1.count("o")
v1_letter = lower_1.count("v")
e11_letter = lower_1.count("e")

t2_letter = lower_2.count("t")
r2_letter = lower_2.count("r")
u2_letter = lower_2.count("u")
e2_letter = lower_2.count("e")
l2_letter = lower_2.count("l")
o2_letter = lower_2.count("o")
v2_letter = lower_2.count("v")
e12_letter = lower_2.count("e")

true_sum_word1 = t1_letter + r1_letter + u1_letter + e1_letter
true_sum_word2 = t2_letter + r2_letter + u2_letter + e2_letter

love_sum_word1 = l1_letter + o1_letter + v1_letter + e11_letter
love_sum_word2 = l2_letter + o2_letter + v2_letter + e12_letter

sum_word_true = true_sum_word1 + true_sum_word2
sum_word_love = love_sum_word1 + love_sum_word2

love_score = str(sum_word_true) + str(sum_word_love)
love_score = int(love_score)

if love_score < 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
