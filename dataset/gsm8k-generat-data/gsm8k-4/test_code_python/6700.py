def solution():
    """Billy's mom sends him to get ketchup. She gives him $10 and tells him to get the best deal on ketchup that he can and to spend all $10 on ketchup. He finds a bottle with 10 oz that cost $1 each. He finds a bottle that costs $2 that contains 16 ounces. He finds a bottle with 25 ounces that costs $2.5. He finds a $5 bottle that contains 50 ounces. Finally, he finds a $10 bottle with 200 ounces. How many bottles of ketchup does he buy?"""
    # Define the available options and their prices and sizes
    options = {
        "Option 1": {"price": 1, "size": 10},
        "Option 2": {"price": 2, "size": 16},
        "Option 3": {"price": 2.5, "size": 25},
        "Option 4": {"price": 5, "size": 50},
        "Option 5": {"price": 10, "size": 200}
    }

    # Define the total budget and initialize the number of bottles purchased
    budget = 10
    num_bottles = 0

    # Sort the options by price per ounce
    sorted_options = sorted(options.items(), key=lambda x: x[1]["price"]/x[1]["size"])

    # Iterate through the options in order and purchase as much as can be afforded within the budget
    for option, data in sorted_options:
        while budget >= data["price"]:
            num_bottles += 1
            budget -= data["price"]
    
    # Return the number of bottles purchased
    result = num_bottles
    return result

print(solution())