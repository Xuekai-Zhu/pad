def solution():
    num_students = 27
    glue_sticks_per_student = 2
    glue_sticks_per_pack = 8

    # Calculate the total number of glue sticks needed
    total_glue_sticks = num_students * glue_sticks_per_student

    # Calculate the number of packs needed
    packs_needed = total_glue_sticks // glue_sticks_per_pack
    if total_glue_sticks % glue_sticks_per_pack!= 0:
        packs_needed += 1

    result = packs_needed
    return result

print(solution())