def solution():
    """Liam is teaching art to a group of 10 students. He has 20 art kits that he hands out to the students to share, 1 art kit for 2 students. From those art kits half the students make 3 artworks each and half the students make 4 artworks each. How many artistic works does the whole class create?"""
    num_students = 10
    num_art_kits = 20
    num_students_per_kit = 2
    total_num_kits_needed = num_students / num_students_per_kit
    extra_kits_needed = total_num_kits_needed - num_art_kits
    if extra_kits_needed > 0:
        num_art_kits_needed = num_art_kits + extra_kits_needed
    else:
        num_art_kits_needed = num_art_kits
    num_students_making_3 = num_students // 2
    num_students_making_4 = num_students - num_students_making_3
    num_artworks_made = (num_students_making_3 * 3) + (num_students_making_4 * 4)
    result = num_artworks_made
    return result

print(solution())