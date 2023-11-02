def solution():
    starting_amount = 80 + 40  # Lizzy's mother gave her 80 cents and her father gave her 40 cents
    candy_cost = 50
    uncle_gift = 70

    # Calculate the total amount of money Lizzy has left
    total_amount = starting_amount - candy_cost + uncle_gift
    result = total_amount
    return result

print(solution())