def solution():
    """Iggy is training for a marathon. On Monday, he runs 3 miles. On Tuesday, he runs 4 miles. On Wednesday, he runs 6 miles. On Thursday, he runs 8 miles. On Friday, he runs 3 miles. Iggy runs at a pace of 1 mile in 10 minutes. What is the total number of hours that Iggy spends running from Monday to Friday?"""
    total_miles = 3 + 4 + 6 + 8 + 3
    pace_minutes_per_mile = 10
    total_minutes = total_miles * pace_minutes_per_mile
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())