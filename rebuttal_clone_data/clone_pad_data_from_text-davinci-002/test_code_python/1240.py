def solution():
     purchase_cost = 42 + 18 + 14
     ounces_purchased = (200 - purchase_cost) / 1.5
     feet_flown = ounces_purchased * 113
     result = feet_flown
     return result

print(solution())