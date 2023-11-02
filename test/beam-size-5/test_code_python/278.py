def solution():
    num_team_members = 12
    num_coaches = 3
    num_guests_per_team_member = 2
    num_guests_per_pizza = 3
    cost_per_pizza = 15

    # Calculate the total number of guests
    total_guests = num_team_members * num_guests_per_team_member

    # Calculate the total number of pizzas
    total_pizzas = total_guests // num_guests_per_pizza

    # Calculate the total cost of all pizzas
    total_cost = total_pizzas * cost_per_pizza
    result = total_cost
    return result

print(solution())