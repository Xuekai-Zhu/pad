def solution():
     food_cost = [10, 20, 30]
     tip_percent = 20
 
     # first we need to calculate the total cost of the meal
     total_cost = sum(food_cost)
 
     # then we need to calculate how much the tip will be
     tip_amount = total_cost * (tip_percent / 100)
 
     # finally, we need to calculate how much each person should pay
     # we can do this by dividing the tip amount by the number of people
     tip_per_person = tip_amount / len(food_cost)
 
     # round the result to 2 decimal places
     tip_per_person = round(tip_per_person, 2)
 
     result = tip_per_person
 
     return result

print(solution())