def solution():
    eggs_per_turtle = 20  # Each turtle lays a clutch of 20 eggs
    hatch_success_rate = 0.4  # 40% of the eggs successfully hatch
    num_turtles = 6  # There are 6 turtles

    # Calculate the total number of hatchlings produced by the turtles
    total_eggs = eggs_per_turtle * num_turtles
    num_hatchlings = total_eggs * hatch_success_rate
    result = num_hatchlings
    return result

print(solution())