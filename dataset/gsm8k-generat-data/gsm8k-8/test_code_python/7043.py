def solution():
    # Calculate the remaining amount of gas bill
    gas_remaining = (40 * 0.25) - 5

    # Calculate the remaining amount of water bill
    water_remaining = 40 * 0.5

    # Calculate the remaining amount of internet bill
    internet_remaining = 25 - (5 * 4)

    # Calculate the total remaining amount
    total_remaining = gas_remaining + water_remaining + internet_remaining

    result = total_remaining
    return result

print(solution())