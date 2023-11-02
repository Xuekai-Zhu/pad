def solution():
    """In a studio audience of 100 people, 40% of these people have an envelope taped underneath their chairs.
    20% of these people will have "You Won" in their envelope, the rest will have empty envelopes. How many people will win a prize?"""
    total_people = 100
    envelopes_with_prize = total_people * 0.4 * 0.2
    result = envelopes_with_prize
    return result

print(solution())