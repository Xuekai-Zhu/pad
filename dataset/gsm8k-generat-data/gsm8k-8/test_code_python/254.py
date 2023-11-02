def solution():
    # Calculate the total number of cars in each section
    section_g_cars = 15 * 10
    section_h_cars = 20 * 9

    # Calculate the total number of cars Nate walked past
    total_cars_walked = section_g_cars + section_h_cars

    # Calculate the time Nate spent searching for his car
    time_spent = total_cars_walked / 11
    result = time_spent
    return result

print(solution())