def solution():
    """Billy's mom sends him to get ketchup. She gives him $10 and tells him to get the best deal on ketchup that he can and to spend all $10 on ketchup. He finds a bottle with 10 oz that cost $1 each. He finds a bottle that costs $2 that contains 16 ounces. He finds a bottle with 25 ounces that costs $2.5. He finds a $5 bottle that contains 50 ounces. Finally, he finds a $10 bottle with 200 ounces. How many bottles of ketchup does he buy?"""
    
    # Calculate the cost per ounce for each option
    option1_cost_per_ounce = 1/10
    option2_cost_per_ounce = 2/16
    option3_cost_per_ounce = 2.5/25
    option4_cost_per_ounce = 5/50
    option5_cost_per_ounce = 10/200
    
    # Create a list of tuples of (cost per ounce, bottle size in ounces, bottle cost)
    options = [(option1_cost_per_ounce, 10, 1), (option2_cost_per_ounce, 16, 2), (option3_cost_per_ounce, 25, 2.5), (option4_cost_per_ounce, 50, 5), (option5_cost_per_ounce, 200, 10)]
    
    # Sort the list by cost per ounce
    options.sort(key=lambda x: x[0])
    
    # Spend all $10 on ketchup
    remaining_money = 10
    total_ounces = 0
    for option in options:
        while remaining_money >= option[2]:
            total_ounces += option[1]
            remaining_money -= option[2]
    
    # Calculate how many bottles were bought based on total ounces
    option1_bottles = total_ounces // 10
    option2_bottles = total_ounces // 16
    option3_bottles = total_ounces // 25
    option4_bottles = total_ounces // 50
    option5_bottles = total_ounces // 200
    bottles_bought = option1_bottles + option2_bottles + option3_bottles + option4_bottles + option5_bottles
    
    result = bottles_bought
    return result

print(solution())