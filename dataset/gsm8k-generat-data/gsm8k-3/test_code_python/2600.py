def solution():
    """Emir wants to buy a dictionary that costs $5, a dinosaur book that costs $11, and a children's cookbook that costs $5. He has saved $19 from his allowance. How much more money does Emir need to buy all three books?"""
    # Define the prices of the books
    DICTIONARY_PRICE = 5
    DINOSAUR_BOOK_PRICE = 11
    COOKBOOK_PRICE = 5

    # Define the amount that Emir has saved
    SAVINGS = 19

    # Calculate the total cost of the books
    total_cost = DICTIONARY_PRICE + DINOSAUR_BOOK_PRICE + COOKBOOK_PRICE

    # Calculate the remaining amount of money needed
    remaining_money = total_cost - SAVINGS

    # Display the remaining amount of money needed
    result = remaining_money
    return result

print(solution())