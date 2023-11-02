def solution():
    brother_letters = 40
    greta_letters = brother_letters + 10
    mother_letters = 2 * (brother_letters + greta_letters)
    total_letters = brother_letters + greta_letters + mother_letters
    result = total_letters
    return result

print(solution())