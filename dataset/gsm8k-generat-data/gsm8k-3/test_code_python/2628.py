def solution():
    """John decides to buy some birds. He got 50 dollars from each of his 4 grandparents. If each bird costs $20, how many wings did all the birds have?"""
    # Define the price of one bird and the number of grandparents
    BIRD_PRICE = 20
    NUM_GRANDPARENTS = 4

    # Calculate the total amount of money John has to spend on birds
    total_money = NUM_GRANDPARENTS * 50

    # Calculate the number of birds John can buy with his total money
    num_birds = total_money // BIRD_PRICE

    # Calculate the total number of wings of all the birds John bought
    total_wings = num_birds * 2

    # Display the total number of wings
    result = total_wings
    return result

print(solution())