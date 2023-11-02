def solution():
    """Iggy is training for a marathon. On Monday, he runs 3 miles. On Tuesday, he runs 4 miles. On Wednesday, he runs 6 miles. On Thursday, he runs 8 miles. On Friday, he runs 3 miles. Iggy runs at a pace of 1 mile in 10 minutes. What is the total number of hours that Iggy spends running from Monday to Friday?"""
    total_distance = 3 + 4 + 6 + 8 + 3
    pace = 10  # minutes per mile
    total_time = total_distance * pace
    total_hours = total_time / 60  # convert minutes to hours
    result = total_hours
    return result

print(solution())