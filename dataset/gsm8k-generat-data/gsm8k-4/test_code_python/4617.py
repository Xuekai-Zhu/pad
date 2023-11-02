def solution():
    """Maggie has an after-school job that pays her $5.00 for every magazine subscription she can sell. She sells 4 to her parents, 1 to her grandfather, 2 to the next-door neighbor and twice that amount to another neighbor. How much money did Maggie earn?"""
    # Define the amount earned for each magazine subscription
    SUBSCRIPTION_EARNINGS = 5

    # Calculate the number of magazine subscriptions sold to each person
    parents_subscriptions = 4
    grandfather_subscriptions = 1
    neighbor1_subscriptions = 2
    neighbor2_subscriptions = 2 * neighbor1_subscriptions

    # Calculate the total number of subscriptions sold
    total_subscriptions = parents_subscriptions + grandfather_subscriptions + neighbor1_subscriptions + neighbor2_subscriptions

    # Calculate the total earnings
    total_earnings = total_subscriptions * SUBSCRIPTION_EARNINGS

    # return the result
    result = total_earnings
    return result

print(solution())