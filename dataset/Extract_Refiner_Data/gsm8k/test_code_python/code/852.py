def solution():
    
    num_students = 27
    num_glue_sticks_per_student = 2
    num_packs = num_students * num_glue_sticks_per_student / 8
    num_extra_glue_sticks = num_glue_sticks_per_student - num_glue_sticks_per_student
    num_packs = num_packs + num_extra_glue_sticks
    result = num_packs
    return result

print(solution())