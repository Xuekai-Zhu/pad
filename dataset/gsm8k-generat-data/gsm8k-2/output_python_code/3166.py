def solution():
    """A soccer ball takes twenty minutes to inflate. Alexia and Ermias are inflating balls, with Alexia inflating 20 balls and Ermias inflating 5 more balls than Alexia. Calculate the total time in minutes they took to inflate all the soccer balls."""
    inflate_time = 20
    alexia_balls = 20
    ermias_balls = alexia_balls + 5
    total_balls = alexia_balls + ermias_balls
    total_inflate_time = total_balls * inflate_time
    result = total_inflate_time
    return result

print(solution())