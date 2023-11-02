def solution():
    """A cattle breeder owns 52 dairy cows. Each cow gives 1000 oz of milk per day. Calculate the amount of milk produced per week by the cows."""
    
    # Define the number of cows and the amount of milk produced per cow per day
    NUM_COWS = 52
    MILK_PER_COW_PER_DAY = 1000

    # Calculate the total amount of milk produced per day
    total_milk_per_day = NUM_COWS * MILK_PER_COW_PER_DAY

    # Calculate the total amount of milk produced per week
    total_milk_per_week = total_milk_per_day * 7

    # Display the total amount of milk produced per week
    result = total_milk_per_week
    return result

print(solution())