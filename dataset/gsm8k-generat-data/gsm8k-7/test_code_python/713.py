def solution():
    num_boys = 10
    boy_popsicles = 15
    num_girls = 12
    girl_popsicles = 12

    # Calculate the total number of popsicle sticks brought by the boys
    total_boy_popsicles = num_boys * boy_popsicles

    # Calculate the total number of popsicle sticks brought by the girls
    total_girl_popsicles = num_girls * girl_popsicles

    # Calculate the difference in popsicle sticks brought by the boys and girls
    difference = total_boy_popsicles - total_girl_popsicles
    result = difference
    return result

print(solution())