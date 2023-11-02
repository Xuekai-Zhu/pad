def solution():
     """Phillip's mother asked him to go to the supermarket to buy some things and gave him $95, so he spent $14 on oranges, $25 on apples and $6 on candy. How much money does he have left?"""
     money_given = 95
     money_spent = 14 + 25 + 6
     money_left = money_given - money_spent
     result = money_left
     return result

print(solution())