def solution():
    cans_recycled = 144
    newspapers_collected = 20

    # Calculate the amount received for recycling cans
    can_money = (cans_recycled // 12) * 0.5

    # Calculate the amount received for collecting newspapers
    newspaper_money = (newspapers_collected // 5) * 1.5

    # Calculate the total amount of money received
    total_money = can_money + newspaper_money
    result = total_money
    return result

print(solution())