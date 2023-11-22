def solution():
    
    team_members = 12
    coaches = 3
    guests_per_team_member = 2
    total_guests = team_members * guests_per_team_member * coaches
    pizzas_needed = total_guests // 3
    cost_per_pizza = 15
    total_cost = pizzas_needed * cost_per_pizza
    result = total_cost
    return result

print(solution())