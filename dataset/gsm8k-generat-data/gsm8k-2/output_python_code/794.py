def solution():
    """On Monday Samson ate 3 sandwiches at lunch and ate twice as many at dinner. The next morning, he felt sick from eating all those sandwiches, so he only ate one sandwich for breakfast. How many more sandwiches in total did Samson eat on Monday than Tuesday?"""
    monday_sandwiches = 3 + 2*3  # 3 sandwiches at lunch and twice as many at dinner
    tuesday_sandwiches = 1
    total_sandwiches = monday_sandwiches - tuesday_sandwiches
    result = total_sandwiches
    return result

print(solution())