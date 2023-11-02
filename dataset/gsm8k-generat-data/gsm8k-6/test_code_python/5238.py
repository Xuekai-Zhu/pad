def solution():
    # Calculate the total amount of money received from recycling cans and newspapers
    cans_money = (144 // 12) * 0.50  # divide by 12 cans and multiply by $0.50
    newspaper_money = (20 // 5) * 1.50  # divide by 5 kg and multiply by $1.50
    total_money = cans_money + newspaper_money
    result = total_money
    return result

print(solution())