def solution():
    money_given_on_Tuesday = 8
    money_given_on_Wednesday = money_given_on_Tuesday * 5
    money_given_on_Thursday = money_given_on_Wednesday + 9
    difference = money_given_on_Thursday - money_given_on_Tuesday
    result = difference
    
    return result

print(solution())