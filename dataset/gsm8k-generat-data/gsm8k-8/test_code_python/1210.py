def solution():
    # Define the variables
    eggs_per_turtle = 20
    hatch_rate = 0.4
    num_turtles = 6

    # Calculate the total number of eggs laid
    total_eggs = eggs_per_turtle * num_turtles

    # Calculate the number of hatchlings produced
    hatchlings = total_eggs * hatch_rate

    result = hatchlings
    return result

print(solution())