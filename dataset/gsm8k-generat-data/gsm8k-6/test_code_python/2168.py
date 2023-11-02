def solution():
    # Calculate the amount raised by friends
    friends_amount = 0.4 * 10000 

    # Calculate the remaining amount after friends raised their share
    remaining_amount = (1 - 0.4) * 10000

    # Calculate the amount raised by family
    family_amount = 0.3 * remaining_amount

    # Calculate the amount saved by the president
    savings_amount = remaining_amount - family_amount

    result = savings_amount
    return result

print(solution())