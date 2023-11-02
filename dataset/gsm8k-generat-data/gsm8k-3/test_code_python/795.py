def solution():
    """On Monday Samson ate 3 sandwiches at lunch and ate twice as many at dinner. The next morning, he felt sick from eating all those sandwiches, so he only ate one sandwich for breakfast. How many more sandwiches in total did Samson eat on Monday than Tuesday?"""
    # Calculate the number of sandwiches Samson ate on Monday
    lunch_sandwiches = 3
    dinner_sandwiches = 2 * lunch_sandwiches
    total_sandwiches_monday = lunch_sandwiches + dinner_sandwiches

    # Calculate the number of sandwiches Samson ate on Tuesday
    breakfast_sandwiches = 1

    # Calculate the difference in sandwiches eaten between Monday and Tuesday
    difference = total_sandwiches_monday - breakfast_sandwiches

    # Display the difference in sandwiches eaten
    result = difference
    return result

print(solution())