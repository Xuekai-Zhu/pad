def solution():
    # Define the original amount Mrs. Smith had
    original_amount = 500
    
    # Calculate the amount Mrs. Smith needed after picking out everything she liked
    needed_amount = 1.4 * original_amount
    
    # Calculate the discount that Mrs. Smith received
    discount = 0.15 * needed_amount
    
    # Calculate the final amount Mrs. Smith needs to pay
    final_amount = needed_amount - discount
    
    # Calculate the amount of money Mrs. Smith still needs
    still_need = final_amount - original_amount
    
    result = still_need
    return result

print(solution())