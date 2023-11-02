def solution():
    # Calculate the total cost of the items
    total_cost = 1.50 + 4.35 + 12.65  # cost of paintbrush, set of paints, and wooden easel
    remaining_money = total_cost - 6.50  # calculate how much more money is needed

    result = round(remaining_money, 2)  # round the answer to 2 decimal places
    return result

print(solution())