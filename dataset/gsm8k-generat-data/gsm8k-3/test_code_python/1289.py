def solution():
    """Gary has 30 grams of gold that cost $15 per gram. Anna has 50 grams of gold for the cost of $20 per gram. How much is the cost of their gold combined?"""
    # Define the cost per gram for each person's gold
    gary_cost_per_gram = 15
    anna_cost_per_gram = 20

    # Define the amount of gold each person has in grams
    gary_grams = 30
    anna_grams = 50

    # Calculate the total cost of Gary's gold
    gary_cost = gary_grams * gary_cost_per_gram

    # Calculate the total cost of Anna's gold
    anna_cost = anna_grams * anna_cost_per_gram

    # Calculate the total cost of both people's gold
    total_cost = gary_cost + anna_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())