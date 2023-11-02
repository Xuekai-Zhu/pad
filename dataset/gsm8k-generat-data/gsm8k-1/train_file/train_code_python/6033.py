def solution():
    """Brendan went fishing with his dad. Brenden caught 8 fish in the morning. He threw 3 back that were too small. He caught 5 more in the afternoon. Brendan’s dad caught 13 fish. How many fish did they catch in all?"""
    brenden_morning_catch = 8
    brenden_threw_back = 3
    brenden_afternoon_catch = 5
    dad_catch = 13
    total_catch = brenden_morning_catch + brenden_afternoon_catch + dad_catch - brenden_threw_back
    result = total_catch
    return result

print(solution())