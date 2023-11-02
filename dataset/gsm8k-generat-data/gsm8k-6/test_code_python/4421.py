def solution():
    # Calculate total money available
    total_money = 6 + 5*6 + 2.5*6  # Lisa has 5 times Patricia's money and double Charlotte's

    # Calculate the money required to buy the card
    money_required = 100

    # Calculate the difference between the required money and total money available
    difference = money_required - total_money
    result = difference
    return result

print(solution())