def solution():
     half_of_Jeromes_money = 43
     money_given_to_Meg = 8
     money_given_to_Bianca = 3 * money_given_to_Meg
     money_left = half_of_Jeromes_money - money_given_to_Meg - money_given_to_Bianca
     result = money_left
     return result

print(solution())