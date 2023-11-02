def solution():
    """Class A is twice as big as Class B. Class A is also a third the size of Class C. If Class B has 20 people in it, how many people are in Class C?"""
    # Define the size of Class B
    class_b_size = 20

    # Calculate the size of Class A
    class_a_size = class_b_size * 2

    # Calculate the size of Class C
    class_c_size = class_a_size * 3

    result = class_c_size
    return result

print(solution())