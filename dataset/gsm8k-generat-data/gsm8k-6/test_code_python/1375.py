def solution():
    # Calculate the total cost of feeding and raising the pigs
    cost = (12 * 10 * 3) + (16 * 10 * 3) # $10 per pig per month for 3 pigs raised for 12 months and 3 pigs raised for 16 months respectively
    
    # Calculate the total revenue from selling the fully grown pigs
    revenue = 6 * 300 # $300 per fully grown pig
    
    # Calculate the total profit earned by the farmer
    profit = revenue - cost
    result = profit
    return result

print(solution())