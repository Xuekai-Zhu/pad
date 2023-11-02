def solution():
    
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