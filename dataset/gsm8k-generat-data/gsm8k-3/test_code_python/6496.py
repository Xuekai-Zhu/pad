def solution():
    """The post office receives 60 letters and 20 packages per day. How many pieces of mail does it handle in six months if all the months have 30 days?"""
    
    # Define the number of days in six months
    DAYS_IN_SIX_MONTHS = 30 * 6
    
    # Calculate the total number of letters handled in six months
    total_letters = 60 * DAYS_IN_SIX_MONTHS
    
    # Calculate the total number of packages handled in six months
    total_packages = 20 * DAYS_IN_SIX_MONTHS
    
    # Calculate the total number of pieces of mail handled
    total_mail = total_letters + total_packages
    
    # Display the total number of pieces of mail handled
    result = total_mail
    return result

print(solution())