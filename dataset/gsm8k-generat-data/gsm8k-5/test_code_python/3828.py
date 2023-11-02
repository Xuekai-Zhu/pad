def solution():
    total_guests = 50  # Total guests in the movie screening
    women = total_guests // 2  # Half of the guests are women
    men = 15  # Given there are 15 men
    children = total_guests - women - men  # Remaining guests are children

    # Calculate the number of men and children who left
    men_left = men // 5
    children_left = 4

    # Calculate the total number of guests who stayed
    total_stayed = total_guests - men_left - children_left
    result = total_stayed
    return result

print(solution())