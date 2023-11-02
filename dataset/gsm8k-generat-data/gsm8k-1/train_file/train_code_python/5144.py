def solution():
    """A class is 40% boys. The rest are girls. Every boy in class gets an 80% on the math test. Every girl gets a 90%. What is the class average on the test?"""
    boys_percent = 40
    girls_percent = 100 - boys_percent
    boys_grade = 80
    girls_grade = 90
    class_average = (boys_percent/100) * boys_grade + (girls_percent/100) * girls_grade
    result = class_average
    return result

print(solution())