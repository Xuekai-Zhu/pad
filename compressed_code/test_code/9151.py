def solution():
    
    derek_money = 40
    dave_money = 50
    derek_spending = 14 + 11 + 5
    dave_spending = 7
    derek_leftover = derek_money - derek_spending
    dave_leftover = dave_money - dave_spending
    difference = dave_leftover - derek_leftover
    result = difference
    return result

print(solution())