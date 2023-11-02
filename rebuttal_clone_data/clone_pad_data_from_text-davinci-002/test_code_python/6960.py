def solution():
    wage = 20
    time_lawn = 1
    time_flowers = 2
    money_lawn = 15
    money_flowers = (wage * time_flowers) - (money_lawn)
    result = money_lawn + money_flowers
    
    return result

print(solution())