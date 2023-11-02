def solution():
    """Ali is a dean of a private school where he teaches one class. John is also a dean of a public school. John has two classes in his school. Each class has 1/8 the capacity of Ali’s class which has the capacity of 120 students. What is the combined capacity of both schools?"""
    ali_capacity = 120
    john_capacity = ali_capacity / 8 * 2
    total_capacity = ali_capacity + john_capacity
    result = total_capacity
    return result

print(solution())