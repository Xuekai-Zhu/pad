def solution():
    cindi_num_pencils = 30 / 0.5  # Cindi bought 60 pencils
    marcia_num_pencils = 2 * cindi_num_pencils  # Marcia bought double the amount Cindi did
    donna_num_pencils = 3 * marcia_num_pencils  # Donna bought 3 times as many as Marcia

    # Total number of pencils bought by both Donna and Marcia
    total_pencils = marcia_num_pencils + donna_num_pencils
    result = total_pencils
    return result

print(solution())