def solution():
    # Calculate the total number of appetizers needed for the guests
    appetizers_needed = 6 * 30  # 6 appetizers per guest for 30 guests

    # Calculate the total number of appetizers Patsy has already made
    appetizers_made = (3 + 2 + 2) * 12  # 3 dozen deviled eggs, 2 dozen pigs in a blanket, and 2 dozen kebabs

    # Calculate the number of dozen appetizers Patsy needs to make
    appetizers_to_make = (appetizers_needed - appetizers_made) / 12

    result = appetizers_to_make
    return result

print(solution())