def solution():
    """Natalia is riding a bicycle for the cycling competition. On Monday she rode 40 kilometers and on Tuesday 50 kilometers. On Wednesday she rode 50% fewer kilometers than the day before. On Thursday she rode as many as the sum of the kilometers from Monday and Wednesday. How many kilometers did Natalie ride in total?"""
    # Calculate the distance Natalia rode on Wednesday
    wed_distance = 0.5 * 50

    # Calculate the distance Natalia rode on Thursday
    thur_distance = 40 + wed_distance

    # Calculate the total distance Natalia rode
    total_distance = 40 + 50 + wed_distance + thur_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())