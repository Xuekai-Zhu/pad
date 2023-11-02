def solution():
    # Define the places Columbus explored
    columbus_explorations = ["Caribbean", "Central America", "South America"]
    # Define the location of Antarctica
    antarctica_location = "southernmost continent"
    # Check if Columbus went to Antarctica
    if antarctica_location not in columbus_explorations:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())