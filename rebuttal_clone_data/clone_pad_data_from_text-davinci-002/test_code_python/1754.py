def solution():
    money_from_bank = 2000
    furniture_cost = 400
    money_given_to_friend = (money_from_bank - furniture_cost) * 3/4
    money_left = money_from_bank - furniture_cost - money_given_to_friend
    result = money_left
    
    return result

print(solution())