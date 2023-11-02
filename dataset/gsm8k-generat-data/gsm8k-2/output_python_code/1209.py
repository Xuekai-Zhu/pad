def solution():
    """Each turtle lays a clutch of 20 eggs. If 40% of the eggs successfully hatch, how many hatchlings do 6 turtles produce?"""
    eggs_per_turtle = 20
    success_rate = 0.4
    total_eggs = 6 * eggs_per_turtle
    hatched_eggs = total_eggs * success_rate
    hatchling_count = hatched_eggs
    result = hatchling_count
    return result

print(solution())