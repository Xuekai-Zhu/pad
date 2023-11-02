def solution():
    """A charity is delivering chicken and rice dinners to a shelter for the hungry. They have a hundred plates to deliver. The rice cost ten cents a plate and the chicken cost forty cents a plate. How many dollars did the charity spend on the food for the dinners?"""
    plates = 100
    rice_cost = 0.10
    chicken_cost = 0.40
    total_cost = (plates * rice_cost) + (plates * chicken_cost)
    result = total_cost
    return result

print(solution())