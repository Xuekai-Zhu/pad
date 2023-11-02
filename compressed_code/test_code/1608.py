def solution():
    
    original_shoe_count = 80
    donation_count = int(original_shoe_count * 0.3)
    remaining_count = original_shoe_count - donation_count
    new_count = remaining_count + 6
    result = new_count
    return result

print(solution())