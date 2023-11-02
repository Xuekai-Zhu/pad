def solution():
    """Molly and her parents love to hang out at the beach on weekends. Molly spent the better part of the day at the beach and saw 100 people join them. At 5:00, 40 people left the beach. What's the total number of people at the beach if they all stayed until evening?"""
    initial_people = 0 # starting with zero since the problem doesn't mention an initial number of people
    increase = 100
    decrease = 40
    final_people = initial_people + increase - decrease
    result = final_people
    return result

print(solution())