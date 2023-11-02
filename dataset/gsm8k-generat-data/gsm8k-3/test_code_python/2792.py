def solution():
    """Liam is teaching art to a group of 10 students. He has 20 art kits that he hands out to the students to share, 1 art kit for 2 students. From those art kits half the students make 3 artworks each and half the students make 4 artworks each. How many artistic works does the whole class create?"""
    # Calculate the number of art kits needed per student by dividing the total number of students by 2
    art_kits_per_student = 20 / 2 / 10 

    # Calculate the number of students who will make 3 artworks each
    students_3_artworks = 10 / 2  

    # Calculate the total number of artworks created by half the students who made 3 artworks each
    total_3_artworks = students_3_artworks * 3 

    # Calculate the number of students who will make 4 artworks each
    students_4_artworks = 10 / 2  

    # Calculate the total number of artworks created by half the students who made 4 artworks each
    total_4_artworks = students_4_artworks * 4 

    # Calculate the total number of artworks created by the whole class
    total_artworks = total_3_artworks + total_4_artworks 

    # Display the total number of artworks created
    result = total_artworks 
    return result

print(solution())