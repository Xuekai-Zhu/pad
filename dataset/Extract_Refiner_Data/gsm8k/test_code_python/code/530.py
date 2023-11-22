def solution():
    
    # Define the number of kids
    num_kids = 20

    # Calculate the number of shells brought by the boys
    boys_shells = 60

    # Calculate the number of shells brought by the girls
    girls_shells = boys_shells + 4 * boys_shells

    # Calculate the number of seashells brought by each girl
    seashells_per_girl = girls_shells / num_kids

    # Display the number of seashells brought by each girl
    result = seashells_per_girl
    return result

print(solution())