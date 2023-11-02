def solution():
    num_students = 10
    num_art_kits = 20
    num_students_per_art_kit = 2

    # Calculate the total number of art kits needed
    total_art_kits_needed = num_students / num_students_per_art_kit

    # Find the minimum number of artworks that each half of the students makes
    min_artworks_per_student = min(3, 4)

    # Calculate the total number of artworks made by one half of the students
    num_half_students = num_students // 2
    total_artworks_half_students = num_half_students * min_artworks_per_student

    # Calculate the total number of artworks made by the other half of the students
    num_other_half_students = num_students - num_half_students
    total_artworks_other_half_students = num_other_half_students * (7 - min_artworks_per_student)

    # Calculate the total number of artworks made by the whole class
    total_artworks = total_artworks_half_students + total_artworks_other_half_students
    result = total_artworks
    return result

print(solution())