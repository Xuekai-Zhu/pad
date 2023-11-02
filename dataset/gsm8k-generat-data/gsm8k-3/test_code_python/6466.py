def solution():
    """The gardener at Parc Municipal ordered 250 tulips, 375 carnations, and 320 roses for spring. Each flower is sold for 2€. Calculate the total expenses."""
    # Define the price of each flower
    PRICE_PER_FLOWER = 2

    # Define the quantity of each flower ordered
    tulip_quantity = 250
    carnation_quantity = 375
    rose_quantity = 320

    # Calculate the total cost
    total_cost = (tulip_quantity + carnation_quantity + rose_quantity) * PRICE_PER_FLOWER

    # Display the total cost
    result = total_cost
    return result

print(solution())