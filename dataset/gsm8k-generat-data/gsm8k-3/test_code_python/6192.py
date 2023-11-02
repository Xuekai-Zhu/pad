def solution():
    """Greg and Sarah have 18 apples that they are going to split evenly. Susan has twice as many apples as Greg will end up with. Mark has 5 fewer apples than Susan. Their mom needs 40 apples to make an apple pie. How many will she have left over?"""
    # Determine the number of apples each person has
    total_apples = 18
    greg_sarah_apples = total_apples/2
    susan_apples = greg_sarah_apples*2
    mark_apples = susan_apples - 5

    # Determine the total number of apples
    total_persons = 4  # including mom
    total_apples += greg_sarah_apples + susan_apples + mark_apples

    # Determine the number of apples left over after making the pie
    apples_left_over = total_apples - 40

    # Display the number of apples left over
    result = apples_left_over
    return result

print(solution())