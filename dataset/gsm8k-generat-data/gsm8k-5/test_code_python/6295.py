def solution():
    cards_transcribed = 200  # Brady transcribed 200 recipe cards
    cents_per_card = 70  # Brady earns 70 cents per card transcribed
    bonus_threshold = 100  # Brady gets a $10 bonus for every 100 cards transcribed
    bonus_amount = 10  # Brady earns a $10 bonus for every 100 cards transcribed

    # Calculate the total earnings from transcribing cards
    earnings = cents_per_card * cards_transcribed / 100

    # Calculate the number of bonuses Brady earned
    num_bonuses = cards_transcribed // bonus_threshold

    # Calculate the total earnings from bonuses
    bonus_earnings = num_bonuses * bonus_amount

    # Add the earnings and bonuses to get the total earnings
    total_earnings = earnings + bonus_earnings
    result = total_earnings
    return result

print(solution())