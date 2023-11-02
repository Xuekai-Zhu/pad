def solution():
    """My mother celebrated her birthday with a total of 60 guests. Half of the guests are women, 15 are men, and the rest are children.
    In the middle of the celebration, 1/3 of the men and 5 children left. How many people stayed and enjoyed the birthday celebration?"""
    # Define the total number of guests and the number of men
    total_guests = 60
    men = 15

    # Calculate the number of women and children
    women = total_guests // 2
    children = total_guests - women - men

    # Calculate the number of people who left the celebration
    men_left = men // 3
    children_left = 5

    # Calculate the number of people who stayed and enjoyed the celebration
    stayed = total_guests - men_left - children_left

    # return the result
    result = stayed
    return result

print(solution())