def solution():
    """Liam is teaching art to a group of 10 students. He has 20 art kits that he hands out to the students to share, 1 art kit for 2 students. From those art kits half the students make 3 artworks each and half the students make 4 artworks each. How many artistic works does the whole class create?"""
    # Define the number of students and art kits
    num_students = 10
    num_kits = 20

    # Calculate the number of students who can share an art kit
    num_students_per_kit = 2

    # Calculate the total number of artwork each group of students can create
    artwork_per_group = (num_kits // num_students_per_kit) * ((num_students // 2) * 3 + (num_students // 2) * 4)

    # Calculate the total number of artwork created by the whole class
    total_artwork = artwork_per_group * 2

    # return the result
    result = total_artwork
    return result

print(solution())