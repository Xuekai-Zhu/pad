def solution():
    mancino_gardens = 3
    mancino_length = 16
    mancino_width = 5

    marquita_gardens = 2
    marquita_length = 8
    marquita_width = 4

    # Calculate the total square footage of Mancino's gardens
    mancino_sq_ft = mancino_gardens * mancino_length * mancino_width

    # Calculate the total square footage of Marquita's gardens
    marquita_sq_ft = marquita_gardens * marquita_length * marquita_width

    # Calculate the combined square footage of all gardens
    total_sq_ft = mancino_sq_ft + marquita_sq_ft
    result = total_sq_ft
    return result

print(solution())