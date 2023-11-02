def solution():
    holy_book = "Quran"
    punctuation_used = "none"
    if holy_book == "Quran" and punctuation_used != "modern":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())