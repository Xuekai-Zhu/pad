def solution():
    # Define the starting number of seashells and the increment
    starting_seashells = 50
    increment = 20

    # Calculate the number of seashells in each week
    week1_seashells = starting_seashells
    week2_seashells = week1_seashells + increment
    week3_seashells = week2_seashells + increment
    week4_seashells = week3_seashells + increment

    # Calculate the total number of seashells in a month
    total_seashells = week1_seashells + week2_seashells + week3_seashells + week4_seashells
    result = total_seashells
    return result

print(solution())