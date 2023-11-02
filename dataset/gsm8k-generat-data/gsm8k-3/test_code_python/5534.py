def solution():
    """Julie wants to give her favorite cousin a $2345 mountain bike for his birthday. So far, she has saved $1500. Since the birthday is still a few weeks away, Julie has time to save even more. She plans on mowing 20 lawns, delivering 600 newspapers, and walking 24 of her neighbors’ dogs. She is paid $20 for each lawn, 40 cents per newspaper, and $15 per dog. After purchasing the bike, how much money will Julie have left?"""
    # Define the cost of the mountain bike
    bike_cost = 2345

    # Define the amount Julie has already saved
    saved_amount = 1500

    # Define the amounts Julie will earn
    lawn_earnings = 20 * 20
    newspaper_earnings = 0.4 * 600
    dog_earnings = 15 * 24

    # Calculate Julie's total earnings
    total_earnings = lawn_earnings + newspaper_earnings + dog_earnings

    # Calculate how much money Julie will have left after purchasing the bike
    left_over = saved_amount + total_earnings - bike_cost

    # Display how much money Julie will have left
    result = left_over
    return result

print(solution())