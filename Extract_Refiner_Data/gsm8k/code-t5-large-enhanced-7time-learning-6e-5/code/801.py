def solution():
    
    # Define the cost of the diamond and gold
    diamond_cost = 600
    gold_cost = 300

    # Calculate the total cost of the ring
    total_cost = diamond_cost + gold_cost

    # Calculate the amount of the premium
    premium = total_cost * 0.3

    # Calculate the total amount paid
    total_paid = total_cost + premium

    # Display the total amount paid
    result = total_paid
    return result

print(solution())