def solution():
    # Calculate the number of art kits each student gets
    art_kits_per_student = 20 / 2 / 10  # 20 kits shared between 2 students each, for 10 students total

    # Calculate the number of students who make 3 artworks and the number who make 4
    num_students_3 = 5  # Half the students make 3 artworks
    num_students_4 = 5  # Half the students make 4 artworks

    # Calculate the total number of artworks created by all students
    total_artworks = (num_students_3 * 3) + (num_students_4 * 4)

    result = total_artworks
    return result

print(solution())