def solution():
    # Define the number of cards Mark has to choose from
    total_cards = 52 - 12  # There are 12 face cards (3 per suit) and 4 8's per suit.
    
    # Define the number of cards that are red and divisible by 3
    red_divisible_by_3 = 2 * 2  # There are 2 red 3's and 2 red 9's
    
    # Calculate the probability of picking a red card divisible by 3
    probability = red_divisible_by_3 / total_cards
    
    # Calculate the expected number of times Mark will pick a red card divisible by 3 in 36 trials
    expected_times = probability * 36
    
    result = expected_times
    return result

print(solution())