def solution():
    """Billy's mom sends him to get ketchup. She gives him $10 and tells him to get the best deal on ketchup that he can and to spend all $10 on ketchup. He finds a bottle with 10 oz that cost $1 each. He finds a bottle that costs $2 that contains 16 ounces. He finds a bottle with 25 ounces that costs $2.5. He finds a $5 bottle that contains 50 ounces. Finally, he finds a $10 bottle with 200 ounces. How many bottles of ketchup does he buy?"""
    # Define the prices and sizes of each bottle of ketchup
    prices = [1, 2, 2.5, 5, 10]
    sizes = [10, 16, 25, 50, 200]

    # Initialize the total amount of ketchup purchased and the remaining budget
    total_ketchup = 0
    remaining_budget = 10

    # Loop through each bottle of ketchup and buy as much as possible within the budget
    for i in range(len(prices)):
        while remaining_budget >= prices[i]:
            total_ketchup += sizes[i]
            remaining_budget -= prices[i]

    # Calculate the number of bottles purchased
    num_bottles = total_ketchup // 16

    # Display the number of bottles purchased
    result = num_bottles
    return result

print(solution())