def solution():
    ticket_price = 10  # Evening ticket cost $10
    combo_price = 10  # Large popcorn & drink combo cost $10

    # Calculate the regular price of ticket and combo
    regular_price = ticket_price + combo_price

    # Calculate the discounted price during special offer hours
    discounted_ticket_price = 10 - (10 * 0.2)  # 20% off on evening tickets from noon to 3 pm
    discounted_combo_price = 10 - (10 * 0.5)  # 50% off on combo from noon to 3 pm

    # Calculate the discounted price of ticket and combo during special offer hours
    discounted_price = discounted_ticket_price + discounted_combo_price

    # Calculate the savings by going to the earlier movie
    savings = regular_price - discounted_price

    result = savings
    return result

print(solution())