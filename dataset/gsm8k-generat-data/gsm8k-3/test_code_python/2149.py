def solution():
    """Ocho has 8 friends and half are girls. His friends who are boys like to play theater with him. How many boys play theater with him?"""
    # Find the number of girls among Ocho's friends
    num_girls = 8 // 2

    # Find the number of boys among Ocho's friends
    num_boys = 8 - num_girls

    # Assume that all boys play theater with Ocho
    boys_play_theater = num_boys

    # Display the number of boys who play theater with Ocho
    result = boys_play_theater
    return result

print(solution())