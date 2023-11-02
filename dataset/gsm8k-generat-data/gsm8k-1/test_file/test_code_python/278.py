def solution():
    """Maddy is buying pizza for her cousin's soccer game. There are 12 team members and 3 coaches. Each team member brings 2 guests. A pizza will serve 3 people. If each pizza costs $15, how many dollars will Maddy spend?"""
    team_members = 12
    coaches = 3
    guests = team_members * 2
    total_people = team_members + coaches + guests
    pizzas_needed = (total_people // 3) + (1 if total_people % 3 != 0 else 0) # round up to account for leftovers
    pizza_cost = 15
    total_cost = pizzas_needed * pizza_cost
    result = total_cost
    return result

print(solution())