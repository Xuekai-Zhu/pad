def solution():
    # Define the saltiness of the Red Sea and the habitat of the yellow perch
    red_sea_saltiness = "one of the saltiest in the world"
    yellow_perch_habitat = "freshwater"
    # Check if it would be unusual to find a yellow perch in the Red Sea
    if yellow_perch_habitat not in red_sea_saltiness:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())