def solution():
    """John reels in 3 crab baskets a week. Each basket holds 4 crabs. He collects crabs twice a week. Each crab sells for $3. How much money does he make?"""
    # Define the number of crab baskets per week and per day
    CRAB_BASKETS_PER_WEEK = 3
    CRAB_BASKETS_PER_DAY = CRAB_BASKETS_PER_WEEK / 2

    # Define the number of crabs per basket
    CRABS_PER_BASKET = 4

    # Define the price per crab
    PRICE_PER_CRAB = 3

    # Calculate the total number of crabs collected per week
    total_crabs = CRAB_BASKETS_PER_WEEK * CRABS_PER_BASKET

    # Calculate the total earnings from selling crabs
    total_earnings = total_crabs * PRICE_PER_CRAB

    result = total_earnings
    return result

print(solution())