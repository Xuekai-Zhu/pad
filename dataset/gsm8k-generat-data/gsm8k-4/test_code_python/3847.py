def solution():
    """All people named Barry are nice, while only half of the people named Kevin are nice. Three-fourths of people named Julie are nice, while 10% of people named Joe are nice. If a crowd contains 24 people named Barry, 20 people named Kevin, 80 people named Julie, and 50 people named Joe, how many nice people are in the crowd?"""
    # Calculate the number of nice people with each name
    barry_nice = 24
    kevin_nice = 20 * 0.5
    julie_nice = 80 * 0.75
    joe_nice = 50 * 0.1

    # Calculate the total number of nice people in the crowd
    total_nice = barry_nice + kevin_nice + julie_nice + joe_nice

    # Return the result
    result = total_nice
    return result

print(solution())