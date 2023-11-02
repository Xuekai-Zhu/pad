def solution():
    # Calculate the total amount of gas used in 10 days
    gas_used = 75*10/50  # Tom's car gets 50 miles to the gallon and he drives 75 miles per day for 10 days
    total_cost = gas_used * 3  # Gas costs $3 per gallon
    result = total_cost
    return result

print(solution())