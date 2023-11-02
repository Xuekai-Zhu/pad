def solution():
    """A shop sells laptops at $600 each and a smartphone at $400. Celine buys two laptops and four smartphones for her children. How much change does she get back if she has $3000?"""
    # Define the prices of laptops and smartphones
    laptop_price = 600
    smartphone_price = 400

    # Define the quantity of laptops and smartphones purchased
    laptops_quantity = 2
    smartphones_quantity = 4

    # Calculate the total cost of the purchase
    total_cost = (laptop_price * laptops_quantity) + (smartphone_price * smartphones_quantity)

    # Calculate the change Celine gets back
    change = 3000 - total_cost

    result = change
    return result

print(solution())