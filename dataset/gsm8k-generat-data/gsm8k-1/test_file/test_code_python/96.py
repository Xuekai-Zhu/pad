def solution():
    """Jerome had 4 friends who came to visit him on a certain day. The first friend pressed on the doorbell 20 times before Jerome opened, the second friend pressed on the doorbell 1/4 times more than Jerome's first friend. The third friend pressed on the doorbell 10 times more than the fourth friend. If the fourth friend pressed on the doorbell 60 times, how many doorbell rings did the doorbell make?"""
    friend1 = 20
    friend2 = friend1 + (friend1 * 0.25)
    friend3 = friend4 + 10
    friend4 = 60
    total_rings = friend1 + friend2 + friend3 + friend4
    result = total_rings
    return result

print(solution())