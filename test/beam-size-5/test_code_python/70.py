def solution():
    marigold_price = 2.74
    petunias_price = 1.87
    begonias_price = 2.12
    num_marigolds = 12
    num_petunias = 9
    num_begonias = 17

    # Calculate the total revenue from selling marigolds
    marigold_revenue = marigold_price * num_marigolds

    # Calculate the total revenue from selling petunias
    petunias_revenue = petunias_price * num_petunias

    # Calculate the total revenue from selling begonias
    begonias_revenue = begonias_price * num_begonias

    # Calculate the total revenue from selling all the pots
    total_revenue = marigold_revenue + petunias_revenue + begonias_revenue
    result = total_revenue
    return result

print(solution())