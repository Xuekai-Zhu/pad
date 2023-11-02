def solution():
    """A jug needs 40 cups of water to be full. A custodian at Truman Elementary School has to fill water jugs for 200 students, who drink 10 cups of water in a day. How many water jugs will the custodian fill with cups of water to provide the students with all the water they need in a day?"""
    cups_per_jug = 40
    cups_per_student_per_day = 10
    total_cups_needed = 200 * cups_per_student_per_day
    jugs_needed = total_cups_needed // cups_per_jug
    if total_cups_needed % cups_per_jug != 0:
        jugs_needed += 1
    result = jugs_needed
    return result

print(solution())