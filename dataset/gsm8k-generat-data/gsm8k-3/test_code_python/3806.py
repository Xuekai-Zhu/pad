def solution():
    """An avant-garde sushi house sells jellyfish for a certain amount and eel for nine times that amount. If the combined cost of one order each kind of sushi is $200, how much does the eel cost?"""
    # Let x be the cost of jellyfish
    # Then the cost of eel is 9x
    # The combined cost is $200, so:
    # x + 9x = $200
    # Simplifying gives:
    # 10x = $200
    # x = $20

    # Therefore, the cost of eel is:
    eel_cost = 9 * 20

    # Display the cost of eel
    result = eel_cost
    return result

print(solution())