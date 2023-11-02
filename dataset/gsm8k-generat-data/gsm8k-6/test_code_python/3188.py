def solution():
    # Find the total number of people eating at Tom's house
    total_people = 1 + 2 + 3  # Tom, his parents, and his 3 siblings

    # Calculate the total number of plates used by each person over 4 days
    plates_per_person = 3 * 2 * 4  

    # Calculate the total number of plates used by Tom and his guests
    total_plates = total_people * plates_per_person
    result = total_plates
    return result

print(solution())