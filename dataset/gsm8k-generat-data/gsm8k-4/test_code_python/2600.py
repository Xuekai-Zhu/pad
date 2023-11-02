def solution():
    """Emir wants to buy a dictionary that costs $5, a dinosaur book that costs $11, and a children's cookbook that costs $5. He has saved $19 from his allowance. How much more money does Emir need to buy all three books?"""
    # Define the prices of the books
    dictionary_price = 5
    dinosaur_book_price = 11
    childrens_cookbook_price = 5

    # Define the amount Emir has saved
    savings = 19

    # Calculate the total cost of the books
    total_cost = dictionary_price + dinosaur_book_price + childrens_cookbook_price

    # Calculate the amount Emir still needs to buy all three books
    remaining_cost = total_cost - savings

    # return the result
    result = remaining_cost
    return result

print(solution())