score = 0
total = 0
print("Welcome to the times tables tester!")
print("What times tables would you like to be tested on?")
times_table = int(input())
print("What is the maximum value for your times table?")
max_value = int(input())
print(f"You will be tested on the {times_table} times tables.")
for x in range(1,max_value + 1):
  print(f"{x} times {times_table} is:")
  answer = int(input())
  if answer == x * times_table:
    print("Correct!")
    score = score + 1
    total = total + 1
  else:
    print("Incorrect.")
    total = total + 1
print(f"You got {score} questions correct out of {total}!")