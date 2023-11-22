def solution():
    
    # Define the amount of milk extracted from a cow and the target amount of milk needed per day
    MILK_PER_COW = 5
    TARGET_AMOUNT = 25

    # Calculate the total amount of milk produced per day
    total_milk_per_day = MILK_PER_COW * 3

    # Calculate the number of cows needed to produce the target amount of milk per day
    cows_needed = TARGET_AMOUNT / MILK_PER_DAY

    # Calculate the number of additional cows needed
    additional_cows_needed = cows_needed - 3

    # Display the number of additional cows needed
    result = additional_cows_needed
    return result

print(solution())