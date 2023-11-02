def solution():
    cost_per_square_foot = 0.10  # $0.10 per square foot
    book_set_cost = 150
    lawn_area_completed = 3 * 20 * 15  # 3 lawns of 20 x 15 square feet each

    # Calculate the total area of lawn that LaKeisha needs to mow to earn enough for the book set
    total_lawn_area_to_mow = book_set_cost / cost_per_square_foot - lawn_area_completed
    result = total_lawn_area_to_mow
    return result

print(solution())