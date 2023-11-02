def solution():
    """Nancy has six pairs of boots, nine more pairs of slippers than boots, and a number of pairs of heels equal to three times the combined number of slippers and boots. How many shoes (individual shoes, not pairs) does she have?"""
    
    # Define the number of pairs of boots
    boots = 6
    
    # Define the number of pairs of slippers
    slippers = boots + 9
    
    # Define the number of pairs of heels
    heels = 3 * (boots + slippers)
    
    # Calculate the total number of individual shoes
    total_shoes = boots * 2 + slippers * 2 + heels * 2
    
    result = total_shoes
    return result

print(solution())