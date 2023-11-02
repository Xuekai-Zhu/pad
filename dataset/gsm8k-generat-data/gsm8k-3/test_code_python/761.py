def solution():
    """Joan is at the grocery store. She has a total of $60 to spend. She is going to purchase 2 containers of hummus, which are $5 each. She is going to purchase chicken for $20, bacon for $10, and vegetables for $10. She wants to purchase apples which are $2 each. With her remaining money, how many apples can she purchase?"""
    
    # Calculate the cost of the hummus
    hummus_cost = 5 * 2
    
    # Calculate the total cost of all the items
    total_cost = hummus_cost + 20 + 10 + 10
    
    # Calculate the amount of money remaining
    remaining_money = 60 - total_cost
    
    # Calculate the number of apples she can purchase with the remaining money
    apples_num = remaining_money // 2

    # Display the number of apples she can purchase
    result = apples_num
    return result

print(solution())