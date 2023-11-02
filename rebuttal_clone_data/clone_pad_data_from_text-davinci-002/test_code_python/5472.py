def solution():
     phone_repair = 11
     laptop_repair = 15
     computer_repair = 18
     phone_repairs = 5
     laptop_repairs = 2
     computer_repairs = 2
     total_repairs = phone_repairs + laptop_repairs + computer_repairs
     total_earned = (phone_repair * phone_repairs) + (laptop_repair * laptop_repairs) + (computer_repair * computer_repairs)
     result = total_earned
     return result

 Question: Candice bowls in a bowling league. Her game scores for the season are 129, 140, 158, 103, 155, and 178. What is her average game score for the season?
 Solution: 
 def solution():
     scores = [129, 140, 158, 103, 155, 178]
     season_average = sum(scores) / len(scores)
     result = season_average
     return result

print(solution())