def solution():
    """Hunter counted 50 cars packed in their school parking lot when entering class one morning. During the first break, he counted 20 more cars in the parking lot. When he got out of class for the lunch break, he realized that 1/2 the number of cars in the parking lot had gone. What's the total number of cars he counted during lunch break?"""
    initial_count = 50
    first_break_count = initial_count + 20
    lunch_break_count = first_break_count / 2
    result = lunch_break_count
    return result

print(solution())