def solution():
    """John reels in 3 crab baskets a week.  Each basket holds 4 crabs.  He collects crabs twice a week.  Each crab sells for $3.  How much money does he make?"""
    # Define the number of crab baskets and crabs
    CRAB_BASKETS = 3
    CRABS_PER_BASKET = 4

    # Define the number of times John collects crabs per week
    COLLECTIONS_PER_WEEK = 2

    # Define the price per crab
    PRICE_PER_CRAB = 3

    # Calculate the total number of crabs John collects per week
    crabs_per_week = CRAB_BASKETS * CRABS_PER_BASKET * COLLECTIONS_PER_WEEK

    # Calculate the total amount of money John makes per week
    total_money = crabs_per_week * PRICE_PER_CRAB

    # Display the total money John makes
    result = total_money
    return result

print(solution())