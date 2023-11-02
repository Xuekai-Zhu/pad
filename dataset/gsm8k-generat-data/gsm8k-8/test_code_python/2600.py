def solution():
    # Define the cost of each book
    dict_cost = 5
    dino_book_cost = 11
    cook_book_cost = 5

    # Calculate the total cost of all three books
    total_cost = dict_cost + dino_book_cost + cook_book_cost

    # Calculate how much more money Emir needs to buy all three books
    money_needed = total_cost - 19

    result = money_needed
    return result

print(solution())