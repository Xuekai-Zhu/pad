def solution():
    """The long jump finals contained four national champions competing against one another. The first competitor jumped a distance of 22 feet. The second competitor jumped one foot farther than the first competitor. The third competitor jumped two feet shorter than the second competitor. And the fourth competitor jumped 3 feet further than the third competitor. How long, in feet, did the fourth competitor jump?"""
    first_jumper = 22
    second_jumper = first_jumper + 1
    third_jumper = second_jumper - 2
    fourth_jumper = third_jumper + 3
    result = fourth_jumper
    return result

print(solution())