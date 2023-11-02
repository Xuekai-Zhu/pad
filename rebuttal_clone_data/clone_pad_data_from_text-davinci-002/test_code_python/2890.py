def solution():
     daves_money = 46
     kyles_money = daves_money * 3 - 12
     kyles_spending = kyles_money / 3
     kyles_money_afterwards = kyles_money - kyles_spending
     result = kyles_money_afterwards
     return result

print(solution())