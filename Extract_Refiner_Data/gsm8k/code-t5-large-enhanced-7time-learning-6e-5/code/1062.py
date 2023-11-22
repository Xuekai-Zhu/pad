def solution():
    
    # Define the initial number of pizzas
    initial_pizzas = 20

    # Calculate the number of pizzas eaten by the glee club
    club_eaten = initial_pizzas * 0.7

    # Calculate the number of pizzas ordered by the football team
    team_ordered = initial_pizzas * 2

    # Calculate the number of pizzas eaten by the football team
    team_eaten = team_ordered * 0.8

    # Calculate the number of pizzas left
    left = initial_pizzas - club_eaten - team_eaten

    # return the result
    result = left
    return result

print(solution())