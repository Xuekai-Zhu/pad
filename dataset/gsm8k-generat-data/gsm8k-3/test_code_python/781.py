def solution():
    """I went to the music shop and there were CDs of The Life Journey for $100, A Day a Life for $50, and When You Rescind for $85 on display. If I bought 3 of each CD to share with my friends, what's the total amount of money I spent in the shop?"""
    # Define the price of each CD
    LIFE_JOURNEY_PRICE = 100
    DAY_IN_LIFE_PRICE = 50
    WHEN_YOU_RESCIND_PRICE = 85

    # Define the number of CDs purchased
    NUM_CDS = 3

    # Calculate the total cost of The Life Journey CDs
    life_journey_cost = LIFE_JOURNEY_PRICE * NUM_CDS

    # Calculate the total cost of A Day in Life CDs
    day_in_life_cost = DAY_IN_LIFE_PRICE * NUM_CDS

    # Calculate the total cost of When You Rescind CDs
    when_you_rescind_cost = WHEN_YOU_RESCIND_PRICE * NUM_CDS

    # Calculate the total cost of all the CDs
    total_cost = life_journey_cost + day_in_life_cost + when_you_rescind_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())