def solution():
    """Lucille is painting her room. Two of her walls are 3 meters wide and 2 meters tall. The third wall is 5 meters wide and 2 meters tall. The final wall is 4 meters wide and 2 meters tall. If each can of paint covers 2 square meters, how many cans of paint does Lucille need?"""
    # Calculate the area of the first two walls
    area1 = 3 * 2 * 2
    area2 = 3 * 2 * 2

    # Calculate the area of the third wall
    area3 = 5 * 2 * 2

    # Calculate the area of the fourth wall
    area4 = 4 * 2 * 2

    # Calculate the total area to be painted
    total_area = area1 + area2 + area3 + area4

    # Calculate the number of cans of paint needed
    cans_of_paint = total_area / 2

    # Display the number of cans of paint needed
    result = cans_of_paint
    return result

print(solution())