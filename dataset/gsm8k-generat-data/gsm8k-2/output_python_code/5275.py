def solution():
    """A 20 person classroom is filled with 40% girls. If 5 new boys join the classroom, what is the new percentage of girls in the class?"""
    total_students = 20
    girls_percentage = 0.4
    boys_percentage = 1 - girls_percentage
    girls_count = int(total_students * girls_percentage)
    boys_count = total_students - girls_count
    new_boys_count = 5
    new_total_students = total_students + new_boys_count
    new_boys_percentage = (boys_count + new_boys_count) / new_total_students
    new_girls_percentage = 1 - new_boys_percentage
    result = new_girls_percentage * 100
    return result

print(solution())