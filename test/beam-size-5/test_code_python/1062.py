def solution():
    
    glee_club_pizzas = 20
    glee_club_eaten = glee_club_pizzas * 0.7
    football_team_pizzas = glee_club_pizzas * 2
    football_team_eaten = football_team_pizzas * 0.8
    total_pizzas = glee_club_eaten + football_team_eaten
    pizzas_left = total_pizzas - total_pizzas
    result = pizzas_left
    return result

print(solution())