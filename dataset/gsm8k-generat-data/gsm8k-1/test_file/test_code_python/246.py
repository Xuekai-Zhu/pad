def solution(): 
    """Each class in a school has 20 students. There are 3 classes. The school as a whole is 50% boys and 50% girls. The first class has 15 girls. The second class has 12 girls. How many boys are in the third class?"""
    class_size = 20
    total_students = class_size * 3
    girls_total = 15 + 12
    boys_total = total_students - girls_total
    boys_each_class = boys_total / 3
    boys_third_class = boys_each_class
    result = boys_third_class
    return result

print(solution())