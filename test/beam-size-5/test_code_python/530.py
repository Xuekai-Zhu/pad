def solution():
    num_kids = 20
    num_boys = 60
    num_girls = num_boys / 4

    # Calculate the total number of shells brought by all boys
    total_boys_shells = num_boys * num_boys

    # Calculate the total number of seashells brought by all girls
    total_girls_shells = total_boys_shells + num_girls

    # Calculate the number of seashells brought by each girl
    seashells_per_girl = total_girls_shells / num_girls
    result = seashells_per_girl
    return result

print(solution())