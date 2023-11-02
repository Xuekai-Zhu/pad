def solution():
    """Trip wanted to watch the new action movie in theaters.  An evening ticket cost $10 and a large popcorn & drink combo would cost him an additional $10.  He noticed on their website, they had a special offer.  From 12 noon to 3 pm, save 20% off tickets and 50% off any food combos.  How much money could Trip save by going to the earlier movie?"""
    # Define the regular prices of tickets and food combo
    TICKET_PRICE = 10
    FOOD_PRICE = 10

    # Calculate the discounted prices during the special offer
    DISCOUNTED_TICKET_PRICE = TICKET_PRICE * 0.8
    DISCOUNTED_FOOD_PRICE = FOOD_PRICE * 0.5

    # Calculate the cost of watching the movie and buying food during regular hours
    REGULAR_COST = TICKET_PRICE + FOOD_PRICE

    # Calculate the cost of watching the movie and buying food during the special offer hours
    DISCOUNTED_COST = DISCOUNTED_TICKET_PRICE + DISCOUNTED_FOOD_PRICE

    # Calculate the amount of money saved by going to the earlier movie
    SAVINGS = REGULAR_COST - DISCOUNTED_COST

    # Display the amount of money saved
    result = SAVINGS
    return result

print(solution())