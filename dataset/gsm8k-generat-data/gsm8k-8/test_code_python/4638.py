def solution():
    # Calculate the cost of Sonja's items
    sonja_cost = 3 + 23

    # Calculate the total cost of Barbara's items
    barbara_cost = 1 * 5 + 2 * 2

    # Calculate the total cost of Mario and Rick's items
    doodles_cost = 2 * 3
    mario_cost = doodles_cost / 2
    rick_cost = doodles_cost / 2
    mario_and_rick_cost = mario_cost + rick_cost

    # Calculate the total cost of the party
    total_cost = sonja_cost + barbara_cost + mario_and_rick_cost + 4

    # Calculate the cost difference between Sonja and the rest of the office
    rest_of_office_cost = barbara_cost + mario_and_rick_cost + 4
    difference = sonja_cost - rest_of_office_cost

    result = difference
    return result

print(solution())