def solution():
    """Three friends went out to watch a movie. Mitch paid for their tickets at $7 each. On the other hand, Jam paid for the 2 boxes of popcorn at $1.5 while Jay paid for the 3 cups of milk tea at $3 each. If the three of them will split the total expenses, how much should each contribute?"""
    # Define the cost of the movie tickets and the snacks
    movie_cost = 7 * 3
    snack_cost = 1.5 * 2 + 3 * 3

    # Calculate the total expense
    total_expense = movie_cost + snack_cost

    # Divide the total expense evenly among the three friends
    each_contribute = total_expense / 3

    # return the result
    result = each_contribute
    return result

print(solution())