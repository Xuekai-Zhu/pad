def solution():
    total_guests = 60  # My mother celebrated her birthday with 60 guests
    women = total_guests / 2  # Half of the guests are women
    men = 15  # 15 of the guests are men
    children = total_guests - women - men  # The rest are children

    # Calculate the number of men and children who left
    men_left = 1/3 * 15  # 1/3 of the men left
    children_left = 5

    # Calculate the number of guests who stayed
    guests_stayed = total_guests - men_left - children_left
    result = guests_stayed
    return result

print(solution())