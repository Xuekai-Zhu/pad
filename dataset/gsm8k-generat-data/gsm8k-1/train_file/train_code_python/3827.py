def solution():
    """There were a total of 50 guests in a movie screening of which half of the guests are women, 15 are men, and the rest are children. In the middle of the movie, 1/5 of the men and 4 children left. How many people stayed?"""
    total_guests = 50
    women = total_guests // 2
    men = 15
    children = total_guests - women - men
    men_left = men // 5
    children_left = 4
    remaining_guests = total_guests - men_left - children_left
    result = remaining_guests
    return result

print(solution())