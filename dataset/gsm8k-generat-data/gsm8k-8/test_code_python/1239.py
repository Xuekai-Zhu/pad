def solution():
    # Define the size of Tom's room
    width = 8
    length = 7

    # Calculate the total area of the room
    area = width * length

    # Calculate the cost of the new floor
    cost_of_new_floor = area * 1.25

    # Add the cost of removing the old floor
    total_cost = cost_of_new_floor + 50
    result = total_cost
    return result

print(solution())