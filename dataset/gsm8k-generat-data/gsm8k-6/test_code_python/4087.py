def solution():
    # Calculate the total amount of money Mitch can spend on the boat
    total_money = 20000 - 500 - 3 * 500  # Mitch needs to keep $500 for license and registration, and 3 times that amount for docking fees
    
    # Calculate the maximum length of boat Mitch can buy
    max_length = total_money // 1500  # A new boat costs $1500 per foot in length
    
    result = max_length
    return result

print(solution())