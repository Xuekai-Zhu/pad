def solution():
    demerits_allowed = 50
    late_demerits = 2 * 6
    joke_demerits = 15
    total_demerits = late_demerits + joke_demerits
    demerits_left = demerits_allowed - total_demerits
    result = demerits_left
    return result

print(solution())