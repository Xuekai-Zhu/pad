def solution():
    eggs_per_turtle = 20
    hatch_success_rate = 0.4
    num_turtles = 6

    # Calculate the total number of eggs laid by all the turtles
    total_eggs = num_turtles * eggs_per_turtle

    # Calculate the number of hatchlings produced from the successfully hatched eggs
    num_hatchlings = total_eggs * hatch_success_rate

    result = num_hatchlings
    return result

print(solution())