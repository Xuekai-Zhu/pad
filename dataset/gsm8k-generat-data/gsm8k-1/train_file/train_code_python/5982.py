def solution():
    """Molly and her parents love to hang out at the beach on weekends. Molly spent the better part of the day at the beach and saw 100 people join them. At 5:00, 40 people left the beach. What's the total number of people at the beach if they all stayed until evening?"""
    initial_count = 0
    join_count = 100
    leave_count = 40
    total_count = initial_count + join_count - leave_count
    result = total_count
    return result

print(solution())