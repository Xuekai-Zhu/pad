def solution():
    elements_for_photosynthesis = ["Hydrogen", "Oxygen", "Carbon"]
    mars_atmosphere = ["Carbon dioxide", "Nitrogen", "Argon", "Water vapor", "Oxygen", "Carbon monoxide", "Hydrogen"]
    for element in elements_for_photosynthesis:
        if element not in mars_atmosphere:
            result = "no"
            break
    else:
        result = "yes"
    return result

print(solution())