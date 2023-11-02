def solution():
    """Jane plans on reading a novel she borrows from her friend. She reads twice a day, once in the morning and once in the evening. In the morning she reads 5 pages and in the evening she reads 10 pages. If she reads at this rate for a week, how many pages will she read?"""
    # Calculate the number of pages read in a day
    pages_per_day = (5 + 10) * 2

    # Calculate the number of pages read in a week
    pages_per_week = pages_per_day * 7

    # Display the number of pages read in a week
    result = pages_per_week
    return result

print(solution())