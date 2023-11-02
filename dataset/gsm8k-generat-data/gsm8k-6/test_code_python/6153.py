def solution():
    # Calculate the total cost of the first 5 books
    first_five = 20 * 5

    # Calculate the total cost of the remaining 15 books
    # After the first 5 books, every additional book receives a $2 discount
    # So the cost for each additional book is $20 - $2 = $18
    remaining_fifteen = 18 * 15

    # Calculate the total cost of all 20 books
    total_cost = first_five + remaining_fifteen
    result = total_cost
    return result

print(solution())