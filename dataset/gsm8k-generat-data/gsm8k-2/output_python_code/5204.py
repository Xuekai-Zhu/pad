def solution():
    """A marathon is 26 miles. He can run the first 10 miles in 1 hour. For the remaining miles he runs at 80% that pace. How long does the race take?"""
    total_miles = 26
    first_10_time = 1
    remaining_miles = total_miles - 10
    remaining_pace = 0.8
    remaining_time = (remaining_miles / remaining_pace) / 60
    total_time = first_10_time + remaining_time
    result = total_time
    return result

print(solution())