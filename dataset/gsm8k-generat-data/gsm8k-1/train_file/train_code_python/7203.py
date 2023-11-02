def solution():
    """A 4th grade class with 20 students and 3 teachers is going to a science museum. The entrance ticket costs $5 each. How much will they pay for the entrance tickets?"""
    students = 20
    teachers = 3
    cost_per_person = 5
    total_people = students + teachers
    total_cost = total_people * cost_per_person
    result = total_cost
    return result

print(solution())