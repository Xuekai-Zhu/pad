def solution():
    """On Monday Samson ate 3 sandwiches at lunch and ate twice as many at dinner. The next morning, he felt sick from eating all those sandwiches, so he only ate one sandwich for breakfast. How many more sandwiches in total did Samson eat on Monday than Tuesday?"""
    # Calculate the number of sandwiches Samson ate on Monday
    sandwiches_monday = 3 + 2*3

    # Calculate the number of sandwiches Samson ate on Tuesday
    sandwiches_tuesday = 1

    # Calculate the difference in the number of sandwiches
    sandwiches_difference = sandwiches_monday - sandwiches_tuesday

    result = sandwiches_difference
    return result

print(solution())