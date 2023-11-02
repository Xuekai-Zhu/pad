def solution():
    """Mr. Jackson’s fourth-grade class has 27 students. He wants to give each student 2 glue sticks. The glue sticks come in packs of 8. How many packs will Mr. Jackson need to buy so every student can have 2 glue sticks, assuming he can only buy whole packs and he expects to have some extra glue sticks left over?"""
    num_students = 27
    glue_per_student = 2
    num_glue_per_pack = 8
    total_glue_needed = num_students * glue_per_student
    num_packs = total_glue_needed // num_glue_per_pack + (1 if total_glue_needed % num_glue_per_pack > 0 else 0)
    result = num_packs
    return result

print(solution())