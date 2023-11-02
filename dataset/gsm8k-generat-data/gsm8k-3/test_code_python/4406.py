def solution():
    """Collin has 25 flowers. Ingrid gives Collin a third of her 33 flowers. If each flower has 4 petals, how many petals does Collin have in total?"""
    # Calculate the number of flowers Collin has after receiving one third of Ingrid's flowers
    total_flowers = 25 + (1/3) * 33

    # Calculate the total number of petals
    total_petals = total_flowers * 4

    # Display the total number of petals
    result = total_petals
    return result

print(solution())