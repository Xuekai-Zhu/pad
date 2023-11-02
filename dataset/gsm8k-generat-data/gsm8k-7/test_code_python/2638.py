def solution():
    total_money = 300  # $3 in cents
    bridget_money = 0

    # Loop through possible amounts of money for Sarah and calculate Bridget's money
    for i in range(total_money // 2):
        sarah_money = i
        bridget_money = sarah_money + 50

        # Check if the total money is correct
        if sarah_money + bridget_money == total_money:
            result = sarah_money
            return result

    # If no valid amount of money for Sarah is found, return None
    return None

print(solution())