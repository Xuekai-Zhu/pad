def solution():
    """Jane plans on reading a novel she borrows from her friend. She reads twice a day, once in the morning and once in the evening. In the morning she reads 5 pages and in the evening she reads 10 pages. If she reads at this rate for a week, how many pages will she read?"""
    morning_pages = 5
    evening_pages = 10
    days_in_week = 7
    total_pages_per_day = morning_pages + evening_pages
    total_pages_per_week = total_pages_per_day * 2 * days_in_week
    result = total_pages_per_week
    return result

print(solution())