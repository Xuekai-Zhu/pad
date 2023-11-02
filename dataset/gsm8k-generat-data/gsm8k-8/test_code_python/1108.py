def solution():
    # Define the card collection ratios
    anton_to_heike_ratio = 3
    ann_to_heike_ratio = 6

    # Calculate the number of cards Heike has
    heike_cards = ann_to_heike_ratio / 6 * 60

    # Calculate the number of cards Anton has
    anton_cards = anton_to_heike_ratio * heike_cards

    # Calculate the number of cards Ann has more than Anton
    ann_anton_difference = 60 - anton_cards

    result = ann_anton_difference
    return result

print(solution())