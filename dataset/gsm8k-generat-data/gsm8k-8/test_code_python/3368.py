def solution():
    # Define the number of baskets and strawberries in each basket picked by Lilibeth
    lilibeth_baskets = 6
    lilibeth_strawberries = 50
    
    # Calculate the total number of strawberries picked by Lilibeth
    lilibeth_total = lilibeth_baskets * lilibeth_strawberries
    
    # Calculate the total number of strawberries picked by Lilibeth and her friends
    total_strawberries = 4 * lilibeth_total
    
    result = total_strawberries
    return result

print(solution())