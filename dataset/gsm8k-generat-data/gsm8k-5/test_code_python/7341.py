def solution():
    cost_of_book_set = 150  # The book set costs $150
    cost_per_square_foot = 0.10  # LaKeisha charges $.10 per square foot
    area_of_lawn_mowed = 3 * (20 * 15)  # LaKeisha has already mowed three 20 x 15 foot lawns

    # Calculate the total cost of the lawns that LaKeisha has already mowed
    cost_of_lawn_mowed = area_of_lawn_mowed * cost_per_square_foot

    # Calculate the remaining cost that LaKeisha needs to earn for the book set
    remaining_cost = cost_of_book_set - cost_of_lawn_mowed

    # Calculate the remaining area of lawn that LaKeisha needs to mow to earn the remaining cost
    remaining_area = remaining_cost / cost_per_square_foot
    result = remaining_area
    return result

print(solution())