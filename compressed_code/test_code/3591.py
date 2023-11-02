def solution():
    
    brother_letters = 40
    greta_letters = brother_letters + 10
    total_letters = brother_letters + greta_letters
    mother_letters = 2 * total_letters
    total_letters_received = brother_letters + greta_letters + mother_letters
    result = total_letters_received
    return result

print(solution())