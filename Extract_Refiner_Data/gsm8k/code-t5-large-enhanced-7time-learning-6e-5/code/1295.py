def solution():
    
    # Define the prices of ice cream, movie tickets, and bracelet
    ice_cream_price = 3.5
    movie_price = 7.5
    bracelet_price = 8.5

    # Calculate the total cost of tickets
    total_tickets_cost = ice_cream_price + movie_price * 2

    # Calculate the total amount spent
    total_spent = total_tickets_cost + bracelet_price

    # Calculate the amount left after paying for tickets and bracelet
    amount_left = 40 - total_spent

    # return the result
    result = amount_left
    return result

print(solution())