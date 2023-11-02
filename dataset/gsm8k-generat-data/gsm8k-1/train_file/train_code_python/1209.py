def solution():
    """Each turtle lays a clutch of 20 eggs. If 40% of the eggs successfully hatch, how many hatchlings do 6 turtles produce?"""
    eggs_per_turtle = 20
    survival_rate = 0.4
    turtles = 6
    hatchlings = eggs_per_turtle * survival_rate * turtles
    result = hatchlings
    return result

print(solution())