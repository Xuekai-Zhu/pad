def solution():
    total_money = 50  # Brian has $50 to spend
    subway_fare = 2 * 3.5  # Brian needs to pay the $3.50 subway fare each way

    # Calculate the amount Brian has left to spend on fruits
    money_left = total_money - subway_fare - 10 - 5  # Brian has already spent $10 on kiwis and half that amount on bananas

    # Calculate the maximum number of apples Brian can buy
    cost_per_dozen = 14
    dozens_affordable = money_left // cost_per_dozen
    max_apples = dozens_affordable * 12
    result = max_apples
    return result

print(solution())