def solution():
    # Calculate the total number of chickens Wendi has
    initial_chickens = 4
    doubled_chickens = 2 * initial_chickens
    chickens_after_dog = doubled_chickens - 1
    final_chickens = chickens_after_dog + (10-4)
    result = final_chickens
    return result

print(solution())