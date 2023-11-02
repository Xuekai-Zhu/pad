def solution():
     dogs_walked_30 = 3 * 5 * 4
     dogs_walked_60 = 6 * 5
     total_dogs_walked = dogs_walked_30 + dogs_walked_60
     money_made_30 = dogs_walked_30 * 15
     money_made_60 = dogs_walked_60 * 20
     total_money_made = money_made_30 + money_made_60
     result = total_money_made
     return result

print(solution())