def solution():
    
    total_singers = 30
    half_singers = total_singers / 2
    remaining_singers = total_singers - half_singers
    second_verse_singers = remaining_singers / 3
    final_singers = total_singers - half_singers - second_verse_singers
    result = final_singers
    return result

print(solution())