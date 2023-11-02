def solution():
    """Gene is sewing a quilt out of old souvenir t-shirts. He has one shirt from each vacation he has been on. Every shirt is its own quilt block. Each row is made of blocks from a different year of vacations. He goes on four vacations a year and has been vacationing since he was 23 years old. He is now 34. How many quilt blocks does he have in total?"""
    vacations_per_year = 4
    years_of_vacationing = 34 - 23
    total_vacations = vacations_per_year * years_of_vacationing
    quilt_blocks = total_vacations
    result = quilt_blocks
    return result

print(solution())