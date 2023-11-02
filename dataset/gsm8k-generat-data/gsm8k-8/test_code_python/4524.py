def solution():
    # Define the starting number of oranges
    starting_oranges = 60

    # Calculate how many oranges Johann has left after eating 10
    remaining_oranges = starting_oranges - 10

    # Calculate how many oranges were stolen by Carson
    stolen_oranges = remaining_oranges / 2

    # Calculate how many oranges Johann has after Carson returns 5
    final_oranges = remaining_oranges - stolen_oranges + 5
    result = final_oranges
    return result

print(solution())