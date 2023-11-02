def solution():
    
    initial_collection = 80
    donation_percent = 30
    donated_pairs = int(initial_collection * (donation_percent / 100))
    remaining_pairs = initial_collection - donated_pairs
    new_pairs = 6
    total_pairs = remaining_pairs + new_pairs
    result = total_pairs
    return result

print(solution())