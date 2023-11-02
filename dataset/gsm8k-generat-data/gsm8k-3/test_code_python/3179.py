def solution():
    """A shop sells laptops at $600 each and a smartphone at $400. Celine buys two laptops and four smartphones for her children. How much change does she get back if she has $3000?"""
    # Define the cost of each item
    LAPTOP_PRICE = 600
    SMARTPHONE_PRICE = 400

    # Define the number of each item purchased
    laptop_count = 2
    smartphone_count = 4

    # Calculate the total cost of the items
    total_cost = (laptop_count * LAPTOP_PRICE) + (smartphone_count * SMARTPHONE_PRICE)

    # Calculate the change
    change = 3000 - total_cost

    # Display the change
    result = change
    return result

print(solution())