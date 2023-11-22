def solution():
    
    # Define the price of the book and the discount percentage
    book_price = 19.5
    discount_percentage = 25

    # Calculate the original price
    original_price = book_price / (1 - discount_percentage/100)

    # Display the original price
    result = original_price
    return result

print(solution())