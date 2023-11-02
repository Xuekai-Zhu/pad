def solution():
    
    max_demerits = 50
    demerits_for_lateness = 2 * 6
    demerits_for_joke = 15
    remaining_demerits = max_demerits - (demerits_for_lateness + demerits_for_joke)
    result = remaining_demerits
    return result

print(solution())