def solution():
    """There were a total of 50 guests in a movie screening of which half of the guests are women, 15 are men, and the rest are children. In the middle of the movie, 1/5 of the men and 4 children left. How many people stayed?"""
    # Calculate the number of women
    women = 50 / 2

    # Calculate the number of children
    children = 50 - (women + 15)

    # Calculate the number of men who left
    men_left = 15 / 5

    # Calculate the number of children who left
    children_left = 4

    # Calculate the total number of people who left
    total_left = men_left + children_left

    # Calculate the number of people who stayed
    stayed = 50 - total_left

    # Display the number of people who stayed
    result = stayed
    return result

print(solution())