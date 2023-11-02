def solution():
    Greta_letters = 2 * brother_letters
    total_letters = Greta_letters + brother_letters
    mother_letters = total_letters * 2
    final_total = Greta_letters + brother_letters + mother_letters
    return final_total

print(solution())