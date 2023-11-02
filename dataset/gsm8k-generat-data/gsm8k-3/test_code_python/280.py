def solution():
    """The price of a home is $98 per square foot (sq ft). The house is 2,400 sq ft and the barn out back is 1,000 sq ft. How much is this property?"""
    # Define the price per square foot
    PRICE_PER_SF = 98

    # Define the size of the house and barn
    house_size = 2400
    barn_size = 1000

    # Calculate the total size of the property
    total_size = house_size + barn_size

    # Calculate the total cost of the property
    total_cost = total_size * PRICE_PER_SF

    # Display the total cost of the property
    result = total_cost
    return result

print(solution())