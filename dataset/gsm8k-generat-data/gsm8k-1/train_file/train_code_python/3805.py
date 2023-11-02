def solution():
    """An avant-garde sushi house sells jellyfish for a certain amount and eel for nine times that amount. If the combined cost of one order each kind of sushi is $200, how much does the eel cost?"""
    total_cost = 200
    jellyfish_cost = total_cost / 10
    eel_cost = jellyfish_cost * 9
    result = eel_cost
    return result

print(solution())