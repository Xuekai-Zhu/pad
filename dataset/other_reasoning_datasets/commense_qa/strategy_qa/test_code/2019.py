def solution():
    num_courses = 4
    num_dishes = "odd"
    num_people = "odd"
    if num_courses % 2 == 0 or num_dishes == "even" or num_people == "even":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())