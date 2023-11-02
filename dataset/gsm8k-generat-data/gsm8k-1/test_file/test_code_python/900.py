def solution():
    """There are 9 Fast and the Furious movies, Deepa has seen each one in the theatre three times. She has spent $216 seeing these movies. What is the average price she paid per ticket?"""
    num_movies = 9
    num_viewings = 3
    total_cost = 216
    num_tickets = num_movies * num_viewings
    average_price = total_cost / num_tickets
    result = average_price
    return result

print(solution())