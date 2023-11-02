def solution():
    # Initial number of boys and girls
    boys = 14
    girls = 10

    # After some drop out
    boys_left = boys - 4
    girls_left = girls - 3

    result = (boys_left, girls_left) # Return a tuple with the number of boys and girls left
    return result

print(solution())