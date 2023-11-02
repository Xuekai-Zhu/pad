def solution():
    num_pictures_per_day = 10
    num_years = 3
    num_days_per_year = 365
    num_cards_per_day = num_pictures_per_day / 50  # each card can store 50 images
    card_cost = 60

    # Calculate the total number of memory cards that John needs
    total_num_cards = num_cards_per_day * num_days_per_year * num_years

    # Calculate the total cost of all memory cards that John needs
    total_cost = total_num_cards * card_cost
    result = total_cost
    return result

print(solution())