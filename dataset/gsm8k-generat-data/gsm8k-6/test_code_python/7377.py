def solution():
    # Calculate the total value of change in dollars and cents
    total_change = 76*0.25 + 85*0.1 + 20*0.05 + 150*0.01

    # Calculate the fee taken by the coin-counting machine
    fee = total_change * 0.1

    # Calculate the final amount of money Darrel will receive
    final_amount = total_change - fee

    result = final_amount
    return result

print(solution())