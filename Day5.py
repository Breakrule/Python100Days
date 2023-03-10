# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
len_list = 0
for panjang in student_heights:
    len_list += 1
print(len_list)

total = 0
for jumlah in student_heights:
    total += jumlah
print(total)

final_result = total / len_list
print(round(final_result))
