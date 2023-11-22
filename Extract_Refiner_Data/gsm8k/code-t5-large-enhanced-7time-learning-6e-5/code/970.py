def solution():
    
    # Define the prices of the books
    DICTIONARY_PRICE = 18
    DINOSAUR_BOOK_PRICE = 13
    COOKBOOK_PRICE = 8

    # Define Tyler's savings
    SAVINGS = 14

    # Calculate the total cost of the books
    total_cost = DICTIONARY_PRICE + DINOSAUR_BOOK_PRICE + COOKBOOK_PRICE

    # Calculate the number of hours Tyler needs to work to afford his books
    hours_needed = (total_cost - SAVINGS) / 5

    # Display the number of hours Tyler needs to work
    result = hours_needed
    return result

print(solution())