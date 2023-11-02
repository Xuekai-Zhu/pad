def solution():
    """At a birthday party, 30% of the guests are married, 50% are single, and the rest are children. If there are 1000 guests, how many more married people are there than children?"""
    # Define the total number of guests
    total_guests = 1000

    # Calculate the number of married guests
    married_guests = total_guests * 0.3

    # Calculate the number of single guests
    single_guests = total_guests * 0.5

    # Calculate the number of children
    children = total_guests - married_guests - single_guests

    # Calculate the difference between the number of married guests and children
    difference = married_guests - children

    # Return the result
    result = difference
    return result

print(solution())