def solution():
    """Andy can get 50 demerits in a month before getting fired. If he got 2 demerits per instance for showing up late 6 times and 15 demerits for making an inappropriate joke, how many more demerits can he get this month before getting fired?"""
    max_demerits = 50
    demerits_for_lateness = 2 * 6
    demerits_for_joke = 15
    remaining_demerits = max_demerits - (demerits_for_lateness + demerits_for_joke)
    result = remaining_demerits
    return result

print(solution())