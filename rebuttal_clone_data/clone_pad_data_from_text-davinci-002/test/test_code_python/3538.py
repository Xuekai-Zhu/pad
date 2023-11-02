def solution():
    money_saved = 10
    money_given_by_mother = 4
    money_given_by_father = 2 * money_given_by_mother
    total_money = money_saved + money_given_by_mother + money_given_by_father
    candy_cost = 0.5
    jelly_bean_cost = 0.2
    num_candies = 14
    num_jelly_beans = 20
    total_cost = candy_cost * num_candies + jelly_bean_cost * num_jelly_beans
    money_left = total_money - total_cost
    result = money_left
    
    return result

print(solution())