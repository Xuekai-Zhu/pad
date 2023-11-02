def solution():
    # Calculate the total amount of milk sold
    total_milk = 4000 * 3.5

    # Calculate the amount of milk purchased
    purchased_milk = total_milk * (2/5)

    # Calculate the refund amount
    refund = total_milk - purchased_milk

    result = refund
    return result

print(solution())