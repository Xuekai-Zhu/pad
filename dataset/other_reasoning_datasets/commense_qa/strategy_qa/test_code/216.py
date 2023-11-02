def solution():
    # Define the size of Dicopomorpha echmepterygis and the lethal dose of Uranium for humans
    insect_size = 0.13 # in mm
    lethal_dose = 50 # in mg
    # Convert insect size to milligrams
    insect_size_mg = (insect_size/10) ** 3
    # Check if eating an insect-sized Uranium pellet would be fatal
    if insect_size_mg >= lethal_dose:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())