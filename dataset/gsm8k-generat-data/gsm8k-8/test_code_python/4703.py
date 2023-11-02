def solution():
    history = 160
    geography = history + 70
    math = (history + geography) / 2
    science = history * 2

    total_pages = history + geography + math + science
    result = total_pages
    return result

print(solution())