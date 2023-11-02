def solution():
    total_turtles = 42  # There are 42 baby sea turtles
    swept_turtles = total_turtles / 3  # One-third of them got swept to the sea 
    remaining_turtles = total_turtles - swept_turtles  # The number of turtles remaining on the sand

    result = remaining_turtles
    return result

print(solution())