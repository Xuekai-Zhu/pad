def solution():
    """Cole hid 3 dozen eggs in the yard for the Easter egg hunt. Lamar finds 5 eggs. Stacy finds twice as many as Lamar. Charlie finds 2 less than Stacy. And Mei finds half as many as Charlie. How many eggs are still hidden in the yard?"""
    eggs_hidden = 3 * 12
    eggs_found = 5 + 2 * 5 + (2 * 5 - 2) + ((2 * 5 - 2) / 2)
    eggs_remaining = eggs_hidden - eggs_found
    result = eggs_remaining
    return result

print(solution())