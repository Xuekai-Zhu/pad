def solution():
    """There were a total of 50 guests in a movie screening of which half of the guests are women, 15 are men, and the rest are children. In the middle of the movie, 1/5 of the men and 4 children left. How many people stayed?"""
    # Define the initial number of guests
    total_guests = 50

    # Calculate the number of women
    women = total_guests // 2

    # Calculate the number of men
    men = 15

    # Calculate the number of children
    children = total_guests - women - men

    # Calculate the number of men who left
    men_left = men // 5

    # Calculate the number of children who left
    children_left = 4

    # Calculate the total number of guests who left
    total_left = men_left + children_left

    # Calculate the number of guests who stayed
    guests_stayed = total_guests - total_left

    # return the result
    result = guests_stayed
    return result

print(solution())