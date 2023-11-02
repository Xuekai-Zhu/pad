def solution():
    """Each turtle lays a clutch of 20 eggs. If 40% of the eggs successfully hatch, how many hatchlings do 6 turtles produce?"""
    # Define the number of eggs per turtle and the percentage that successfully hatch
    eggs_per_turtle = 20
    hatch_success_rate = 0.4

    # Calculate the total number of eggs laid by 6 turtles
    total_eggs = eggs_per_turtle * 6

    # Calculate the number of hatchlings produced
    hatchlings = total_eggs * hatch_success_rate

    # Return the result
    result = hatchlings
    return result

print(solution())