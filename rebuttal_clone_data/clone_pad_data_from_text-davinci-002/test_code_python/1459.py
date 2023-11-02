def solution():
     people_in_house = 3
     cups_of_coffee_drank_per_person = 2
     ounces_of_coffee_per_cup = 0.5
     total_ounces_of_coffee = people_in_house * cups_of_coffee_drank_per_person * ounces_of_coffee_per_cup
     price_per_ounce = 1.25
     total_price = total_ounces_of_coffee * price_per_ounce
     result = total_price
     return result

print(solution())