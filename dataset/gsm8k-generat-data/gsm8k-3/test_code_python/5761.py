def solution():
    """A farmer has 52 cows. Each cow gives 5 liters of milk a day. How many liters of milk does the farmer get in a week?"""
    # Define the number of cows and liters of milk per cow
    NUM_COWS = 52
    MILK_PER_COW = 5

    # Calculate the total liters of milk per week
    total_liters = NUM_COWS * MILK_PER_COW * 7

    # Display the total liters of milk
    result = total_liters
    return result

print(solution())