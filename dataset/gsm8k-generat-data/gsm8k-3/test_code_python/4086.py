def solution():
    """The number of dishes Sandrine washed was 10 more than the number of bananas Charles cooked. Also, the number of bananas Charles cooked was 3 times the number of pears he picked. If Charles picked 50 pears, how many dishes did Sandrine wash?"""
    # Define the number of pears Charles picked
    pears_picked = 50

    # Calculate the number of bananas Charles cooked
    bananas_cooked = 3 * pears_picked

    # Calculate the number of dishes Sandrine washed
    dishes_washed = bananas_cooked + 10

    # Display the number of dishes Sandrine washed
    result = dishes_washed
    return result

print(solution())