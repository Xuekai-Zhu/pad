def solution():
    # Calculate the number of students who can share the art kits
    sharing_students = 20 * 2  # 1 art kit is for 2 students

    # Calculate the number of students who make 3 artworks each
    students_3_artworks = sharing_students // 2  # Half of the students make 3 artworks each

    # Calculate the number of students who make 4 artworks each
    students_4_artworks = sharing_students // 2  # Half of the students make 4 artworks each

    # Calculate the total number of artworks created by the whole class
    total_artworks = students_3_artworks * 3 + students_4_artworks * 4

    result = total_artworks
    return result

print(solution())