def solution():
    """An avant-garde sushi house sells jellyfish for a certain amount and eel for nine times that amount. If the combined cost of one order each kind of sushi is $200, how much does the eel cost?"""
    jellyfish_cost = x
    eel_cost = 9 * jellyfish_cost
    total_cost = jellyfish_cost + eel_cost
    # We know that: jellyfish_cost + eel_cost = $200
    # Therefore: jellyfish_cost + 9*jellyfish_cost = $200
    # Simplifying: 10*jellyfish_cost = $200
    # Solving for jellyfish_cost:
    jellyfish_cost = 20
    eel_cost = 9 * jellyfish_cost
    result = eel_cost
    return result

print(solution())