def solution():
    """On Monday Samson ate 3 sandwiches at lunch and ate twice as many at dinner. The next morning, he felt sick from eating all those sandwiches, so he only ate one sandwich for breakfast. How many more sandwiches in total did Samson eat on Monday than Tuesday?"""
    monday_lunch = 3
    monday_dinner = monday_lunch * 2
    monday_total = monday_lunch + monday_dinner
    tuesday_breakfast = 1
    tuesday_total = tuesday_breakfast
    difference = monday_total - tuesday_total
    result = difference
    return result

print(solution())