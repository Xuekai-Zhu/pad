def solution():
    """ Lily bought a Russian nesting doll as a souvenir. The biggest doll is 243 cm tall, and each doll is 2/3rd the size of the doll that contains it. How big is the 6th biggest doll?"""
    # Define the height of the biggest doll and the size ratio
    biggest_doll = 243
    size_ratio = 2/3

    # Calculate the heights of all the dolls
    doll_heights = [biggest_doll * size_ratio**n for n in range(6)]

    # Display the height of the 6th biggest doll
    result = round(doll_heights[5], 2)
    return result

print(solution())