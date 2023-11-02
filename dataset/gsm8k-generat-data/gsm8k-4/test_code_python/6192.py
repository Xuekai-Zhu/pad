def solution():
    """Greg and Sarah have 18 apples that they are going to split evenly. Susan has twice as many apples as Greg will end up with. Mark has 5 fewer apples than Susan. Their mom needs 40 apples to make an apple pie. How many will she have left over?"""
    # Split the 18 apples evenly between Greg and Sarah
    greg_and_sarah = 18 / 2
    # Find out how many apples Greg will end up with (half of 18)
    greg = greg_and_sarah / 2
    # Find out how many apples Susan will have (twice as many as Greg)
    susan = greg * 2
    # Find out how many apples Mark will have (5 fewer than Susan)
    mark = susan - 5
    # Calculate the total number of apples
    total_apples = greg + susan + mark
    # Calculate how many apples are left over after making the apple pie
    left_over_apples = total_apples - 40
    result = left_over_apples
    return result

print(solution())