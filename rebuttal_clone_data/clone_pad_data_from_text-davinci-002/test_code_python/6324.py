def solution():
    bottles = 80
    money = 15
    bottle_deposit = 10
    can_deposit = 5
    total_cans = (money - (bottles * bottle_deposit)) / can_deposit
    result = total_cans
    return result

print(solution())