def solution():
    """Sally teaches elementary school and is given $320 to spend on books for her students. A reading book costs $12 and there are 30 students in her class. Unfortunately, if the money she is given by the school to pay for books is not sufficient, she will need to pay the rest out of pocket. How much money does Sally need to pay out of pocket, to buy every student a reading book?"""
    total_money = 320
    cost_per_book = 12
    num_students = 30
    total_cost = cost_per_book * num_students
    if total_cost <= total_money:
        result = 0
    else:
        result = total_cost - total_money
    return result

print(solution())