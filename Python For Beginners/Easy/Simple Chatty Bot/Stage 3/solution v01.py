# Ref: https://hyperskill.org/projects/97/stages/536/implement
bot_name = "Aid"
birth_year = 2020

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
print("Please, remind me your name.")
print(f'What a great name you have, {input()}')

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
rem3, rem5, rem7 = int(input()), int(input()), int(input())
his_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print(f"Your age is {his_age}; that's a good time to start programming!")
