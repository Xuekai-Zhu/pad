def solution():
    """At a birthday party, 30% of the guests are married, 50% are single, and the rest are children. If there are 1000 guests, how many more married people are there than children?"""
    # Define the percentages of guests who are married, single, and children
    MARRIED_PERCENTAGE = 0.3
    SINGLE_PERCENTAGE = 0.5

    # Calculate the number of married and single guests
    married_guests = MARRIED_PERCENTAGE * 1000
    single_guests = SINGLE_PERCENTAGE * 1000

    # Calculate the number of children
    children = 1000 - married_guests - single_guests

    # Calculate the difference between the number of married guests and children
    married_children_diff = married_guests - children

    # Display the difference
    result = married_children_diff
    return result

print(solution())