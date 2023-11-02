def solution():
    """A cattle breeder owns 52 dairy cows. Each cow gives 1000 oz of milk per day. Calculate the amount of milk produced per week by the cows."""

    # Define the number of cows and the amount of milk produced per cow per day
    num_cows = 52
    milk_per_cow_per_day = 1000

    # Calculate the total amount of milk produced per day
    total_milk_per_day = num_cows * milk_per_cow_per_day

    # Calculate the total amount of milk produced per week
    total_milk_per_week = total_milk_per_day * 7

    # Return the result in gallons
    result = total_milk_per_week / 128
    return result

print(solution())