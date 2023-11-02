def solution():
    # Define the initial amount of oranges
    initial_oranges = 10

    # Add the 5 kgs for the neighbor
    total_oranges = initial_oranges + 5

    # Double the amount of oranges for the next two weeks
    for i in range(2):
        total_oranges *= 2

    # Calculate the total amount of oranges after three weeks
    total_oranges *= 3
    result = total_oranges
    return result

print(solution())