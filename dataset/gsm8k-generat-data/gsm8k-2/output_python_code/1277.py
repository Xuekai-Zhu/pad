def solution():
    """The green piece of yarn is 156 cm long. The red yarn is 8 cm more than three times the length of the green yarn. What is the number of centimeters in the total length for the 2 pieces of yarn?"""
    green_yarn_length = 156
    red_yarn_length = 3 * green_yarn_length + 8
    total_length = green_yarn_length + red_yarn_length
    result = total_length
    return result

print(solution())