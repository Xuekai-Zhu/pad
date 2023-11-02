def solution():
    """In a certain school, two classes have a total of 80 students. Each class has the same amount of students, and in each class 40% of the students are girls. How many boys are in each class?"""
    total_students = 80
    girls_percent = 40
    girls_total = total_students * (girls_percent / 100)
    boys_total = total_students - girls_total
    boys_per_class = boys_total / 2
    result = boys_per_class
    return result

print(solution())