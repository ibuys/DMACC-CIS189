"""
average_scores.py

Prompt user for:
    - first name
    - last name
    - age
    - three scores out of 100. 

Compute average of three scores and return the final result as:

{last_name}, {first_name} age: {age} average grade: avg_grade
"""

from statistics import mean

NUMBER_SCORES = 3

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = input("Enter age: ")
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))

# Put scores in list. 
all_scores = [score1, score2, score3]

# Compute average score.
avg_score = round(mean(all_scores), 2)

print(f"{last_name}, {first_name} age: {age} average grade: {avg_score}")

