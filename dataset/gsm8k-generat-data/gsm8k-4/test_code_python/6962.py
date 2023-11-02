def solution():
    """Keanu bought some fish from the store for his pets. He gave his cat half as many fish as he gave to his dog. If he gave his dog 40 fish, and each fish cost him $4, calculate the total amount of money he spent at the store to buy all the fish."""
    # Define the number of fish Keanu's dog received
    dog_fish = 40

    # Calculate the total number of fish Keanu bought
    total_fish = dog_fish * 2

    # Calculate the total amount of money Keanu spent
    total_cost = total_fish * 4

    # Return the result
    result = total_cost
    return result

print(solution())