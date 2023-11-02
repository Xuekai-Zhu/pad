def solution():
    """Nina has received a scholarship worth $8000 less than Kelly's amount. Kelly received a scholarship worth twice the amount Wendy received. How much money did they receive in scholarship together if Wendy received a scholarship worth $20000?"""
    
    # Define the amount Wendy received
    wendy_amount = 20000
    
    # Calculate Kelly's amount
    kelly_amount = 2 * wendy_amount
    
    # Calculate Nina's amount
    nina_amount = kelly_amount - 8000
    
    # Calculate the total amount of scholarship received
    total_amount = wendy_amount + kelly_amount + nina_amount
    
    # Display the total amount of scholarship received
    result = total_amount
    return result

print(solution())