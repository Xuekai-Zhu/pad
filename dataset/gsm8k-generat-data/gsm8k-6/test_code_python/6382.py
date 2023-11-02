def solution():
    # Calculate the total number of children in the camp
    total_children = 14 + 16 + 12 + (14+16+12)/2  # the fourth group has half the number of the first three groups combined

    # Calculate the total number of water bottles needed for 3 days
    total_bottles_needed = total_children * 3 * 3  # each child needs 3 bottles a day for 3 days

    # Calculate the total number of water bottles available from 13 cases
    total_bottles_available = 24 * 13

    # Calculate the remaining number of water bottles needed
    remaining_bottles_needed = total_bottles_needed - total_bottles_available

    result = remaining_bottles_needed
    return result

print(solution())