def solution():
    # Define the normal number of trading cards sold per month
    normal_cards_sold = 21122
    
    # Calculate the number of trading cards sold in June
    june_cards_sold = normal_cards_sold + 3922
    
    # Calculate the total number of trading cards sold in June and July
    june_july_cards_sold = june_cards_sold + normal_cards_sold
    
    result = june_july_cards_sold
    return result

print(solution())