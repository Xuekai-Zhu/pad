def solution():
    """The long jump finals contained four national champions competing against one another. The first competitor jumped a distance of 22 feet. The second competitor jumped one foot farther than the first competitor. The third competitor jumped two feet shorter than the third competitor. And the fourth competitor jumped 3 feet further than the third competitor. How long, in feet, did the fourth competitor jump?"""
    first_jump = 22
    second_jump = first_jump + 1
    third_jump = second_jump - 2
    fourth_jump = third_jump + 3
    result = fourth_jump
    return result

print(solution())