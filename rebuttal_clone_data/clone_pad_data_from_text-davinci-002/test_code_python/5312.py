def solution():
    shirts_sold = 5
    pants_sold = 5
    shirt_price = 1
    pants_price = 3
    total_money = shirts_sold * shirt_price + pants_sold * pants_price
    money_given_to_parents = total_money / 2
    money_left = total_money - money_given_to_parents
    result = money_left
    return result

print(solution())