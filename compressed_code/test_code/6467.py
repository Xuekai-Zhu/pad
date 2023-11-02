def solution():
    
    initial_singers = 30
    first_verse = initial_singers / 2
    second_verse = (initial_singers - first_verse) / 3
    final_verse = initial_singers - first_verse - second_verse
    result = final_verse
    return result

print(solution())