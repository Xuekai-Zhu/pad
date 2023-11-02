def solution():
    dictionary_cost = 5
    dinosaur_book_cost = 11
    children_cookbook_cost = 5
    total_saved = 19

    # Calculate the total cost of all three books
    total_cost = dictionary_cost + dinosaur_book_cost + children_cookbook_cost

    # Calculate how much more money Emir needs to buy all three books
    remaining_cost = total_cost - total_saved
    result = remaining_cost
    return result

print(solution())