def solution():
    
    max_demerits = 50
    late_demerits = 6 * 2
    joke_demerits = 15
    total_demerits = late_demerits + joke_demerits
    remaining_demerits = max_demerits - total_demerits
    result = remaining_demerits
    return result

print(solution())