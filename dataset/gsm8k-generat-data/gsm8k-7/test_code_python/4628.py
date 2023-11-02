def solution():
    brother_letters = 40
    greta_letters = brother_letters + 10
    mother_letters = (brother_letters + greta_letters) * 2
    total_letters = brother_letters + greta_letters + mother_letters
    result = total_letters
    return result

print(solution())