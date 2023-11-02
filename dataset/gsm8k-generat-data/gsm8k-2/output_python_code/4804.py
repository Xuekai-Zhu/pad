def solution():
    """On the island of Castor, there are 40 chess players. A quarter of the island's chess players have never lost to an AI. How many people on the island have lost to a computer, at least once?"""
    total_players = 40
    never_lost = total_players / 4
    lost_to_computer = total_players - never_lost
    result = lost_to_computer
    return result

print(solution())