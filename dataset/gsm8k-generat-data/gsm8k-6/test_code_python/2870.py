def solution():
    # Calculate the cost of the roses
    cost_per_rose = 2  # cost of roses per piece
    total_cost = 300  # total amount Hanna has
    num_roses = total_cost // cost_per_rose  # calculate the number of roses Hanna can buy
    
    # Calculate the number of roses each friend receives
    roses_jenna = num_roses // 3  # Jenna receives 1/3 of the roses
    roses_imma = num_roses // 2  # Imma receives 1/2 of the roses
    
    # Calculate the total number of roses Hanna gives to her friends
    total_roses = roses_jenna + roses_imma
    
    result = total_roses
    return result

print(solution())