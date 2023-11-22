def solution():
    
    # Define the total allowance and the number of weeks Ryan completed his chores
    total_allowance = 6 * 3
    total_weeks = 3

    # Calculate the total cost of the ice cream cones
    ice_cream_cost = 1.25 * 2 + 3 * 1.25

    # Calculate the total cost of going to the movies
    movie_cost = 6.5

    # Calculate the number of movie tickets Ryan can buy
    movie_tickets = total_allowance // movie_cost

    # Display the number of movie tickets Ryan can buy
    result = movie_tickets
    return result

print(solution())