def solution():
    """My mother celebrated her birthday with a total of 60 guests. Half of the guests are women, 15 are men, and the rest are children. In the middle of the celebration, 1/3 of the men and 5 children left. How many people stayed and enjoyed the birthday celebration?"""
    total_guests = 60
    women = total_guests / 2
    men = 15
    children = total_guests - women - men
    men_left = men / 3
    children_left = 5
    guests_left = men_left + children_left
    guests_stayed = total_guests - guests_left
    result = guests_stayed
    return result

print(solution())