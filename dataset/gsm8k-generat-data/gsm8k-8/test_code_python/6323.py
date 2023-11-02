def solution():
    # Define the initial number of jellybeans
    initial_jellybeans = 90

    # Calculate the number of jellybeans left after Samantha and Shelby took some
    jellybeans_left = initial_jellybeans - 24 - 12

    # Calculate the amount of jellybeans Shannon refilled the jar with
    refill_amount = (24 + 12) / 2

    # Calculate the new total number of jellybeans
    new_total = jellybeans_left + refill_amount

    result = new_total
    return result

print(solution())