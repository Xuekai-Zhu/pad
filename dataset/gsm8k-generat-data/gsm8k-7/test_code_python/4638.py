def solution():
    sonja_bread_cost = 3
    sonja_cold_cuts_cost = 23

    num_people = 5
    barbara_soda_cost = num_people
    barbara_crackers_cost = 2 * 2

    mario_rick_cheese_doodles_cost = 2 * 3 / 2

    danica_paper_plates_cost = 4

    # Calculate the total cost of all items
    total_cost = sonja_bread_cost + sonja_cold_cuts_cost + barbara_soda_cost + barbara_crackers_cost + \
                 mario_rick_cheese_doodles_cost + danica_paper_plates_cost

    # Calculate the cost difference between Sonja and the rest
    rest_cost = total_cost - sonja_bread_cost - sonja_cold_cuts_cost
    difference_cost = sonja_bread_cost + sonja_cold_cuts_cost - rest_cost
    result = difference_cost
    return result

print(solution())