def solution():
    """Molly and her parents love to hang out at the beach on weekends. Molly spent the better part of the day at the beach and saw 100 people join them. At 5:00, 40 people left the beach. What's the total number of people at the beach if they all stayed until evening?"""
    # Define the initial number of people at the beach
    initial_people = 0

    # Molly and her parents were already at the beach
    initial_people += 3

    # 100 more people joined them earlier in the day
    initial_people += 100

    # At 5:00, 40 people left the beach
    final_people = initial_people - 40

    result = final_people
    return result

print(solution())