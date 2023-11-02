def solution():
    """James makes potatoes for a group. Each person eats 1.5 pounds of potatoes. He makes potatoes for 40 people. A 20-pound bag of potatoes costs $5. How much does it cost?"""
    # Define the amount of potatoes needed
    potatoes_needed = 40 * 1.5

    # Define the weight of potatoes in each 20-pound bag
    weight_per_bag = 20

    # Calculate the number of bags needed
    bags_needed = potatoes_needed / weight_per_bag

    # Calculate the total cost of the bags needed
    cost = bags_needed * 5
    
    result = cost
    return result

print(solution())