def solution():
    """Andy can get 50 demerits in a month before getting fired. If he got 2 demerits per instance for showing up late 6 times and 15 demerits for making an inappropriate joke, how many more demerits can he get this month before getting fired?"""
    max_demerits = 50
    late_demerits = 6 * 2
    joke_demerits = 15
    total_demerits = late_demerits + joke_demerits
    remaining_demerits = max_demerits - total_demerits
    result = remaining_demerits
    return result

print(solution())