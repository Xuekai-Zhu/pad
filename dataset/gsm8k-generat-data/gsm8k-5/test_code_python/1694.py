def solution():
    length = 600  # The warehouse is 600 feet long
    width = 400  # The warehouse is 400 feet wide
    perimeter = 2 * (length + width)  # The perimeter of the warehouse is 2 times the sum of length and width
    times_to_patrol = 10 - 2  # Carson patrols the warehouse 10 times but skips 2 times
    total_distance = perimeter * times_to_patrol  # Carson walks the perimeter each time he patrols
    result = total_distance
    return result

print(solution())