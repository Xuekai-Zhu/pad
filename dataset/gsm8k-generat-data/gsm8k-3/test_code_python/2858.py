def solution():
    """My mother celebrated her birthday with a total of 60 guests. Half of the guests are women, 15 are men, and the rest are children. In the middle of the celebration, 1/3 of the men and 5 children left. How many people stayed and enjoyed the birthday celebration?"""
    # Define the total number of guests
    total_guests = 60

    # Calculate the number of women
    women = total_guests // 2

    # Calculate the number of children
    children = total_guests - women - 15

    # Calculate the number of men who left
    men_left = 15 // 3

    # Calculate the number of children who left
    children_left = 5

    # Calculate the number of guests who stayed
    guests_stayed = total_guests - men_left - children_left

    # Display the number of guests who stayed
    result = guests_stayed
    return result

print(solution())