def solution():
    # Define the number of times Helen cuts her lawn per month
    cuts_per_month = [2, 2, 4, 4, 4, 4, 2]

    # Define the number of times Helen needs to refill her gas tank
    refills = sum([1 for i in range(len(cuts_per_month)) if (i+1) % 4 == 0])

    # Calculate the total gallons of gas needed for the non-refill cuts
    non_refill_cuts = sum(cuts_per_month) - (2 * refills)
    non_refill_gas = non_refill_cuts * 0.5

    # Calculate the total gallons of gas needed including refills
    total_gas = non_refill_gas + refills * 2

    result = total_gas
    return result

print(solution())