def solution():
    """Monica is a teacher. She has 6 classes per day. The first class has 20 students. 
    The second and third classes have 25 students. Her fourth class has half as many as her first class. 
    Her fifth and sixth classes have 28 students. How many students does Monica see each day?"""
    first_class = 20
    second_class = 25
    third_class = 25
    fourth_class = first_class / 2
    fifth_class = 28
    sixth_class = 28
    total_students = first_class + second_class + third_class + fourth_class + fifth_class + sixth_class
    result = total_students
    return result

print(solution())