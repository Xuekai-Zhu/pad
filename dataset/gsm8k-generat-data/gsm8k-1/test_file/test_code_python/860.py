def solution():
    """George, a grade six teacher, ordered 600 burritos for the sixth-grade class picnic. If there were 50 students at the picnic, and each student was given ten burritos, with Mr. George eating 20 of them, calculate the total number of leftover burritos from the picnic?"""
    total_burritos = 600
    students = 50
    burritos_per_student = 10
    burritos_eaten_by_george = 20
    total_burritos_given = students * burritos_per_student + burritos_eaten_by_george
    leftovers = total_burritos - total_burritos_given
    result = leftovers
    return result

print(solution())