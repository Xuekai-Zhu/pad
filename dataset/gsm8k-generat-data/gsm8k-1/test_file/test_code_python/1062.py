def solution():
    """The glee club ordered 20 pizzas and ate 70% of them. The football team ordered twice as many pizzas and ate 80% of them. How many pizzas are left?"""
    glee_pizzas = 20
    glee_eaten = glee_pizzas * 0.7
    football_pizzas = glee_pizzas * 2
    football_eaten = football_pizzas * 0.8
    total_pizzas = glee_pizzas + football_pizzas - (glee_eaten + football_eaten)
    result = total_pizzas
    return result

print(solution())