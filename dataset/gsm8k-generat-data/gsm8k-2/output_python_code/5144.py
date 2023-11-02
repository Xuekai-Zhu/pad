def solution():
    """A class is 40% boys. The rest are girls. Every boy in class gets an 80% on the math test. Every girl gets a 90%. What is the class average on the test?"""
    boys_percent = 0.4
    girls_percent = 1 - boys_percent

    boys_grade = 0.8
    girls_grade = 0.9

    class_average = (boys_percent * boys_grade) + (girls_percent * girls_grade)
    result = class_average
    return result

print(solution())