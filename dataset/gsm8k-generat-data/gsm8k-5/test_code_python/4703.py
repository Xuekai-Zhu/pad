def solution():
    # Calculate the number of pages in each textbook
    history = 160
    geography = history + 70
    math = (history + geography) / 2
    science = history * 2

    # Calculate the total number of pages
    total_pages = history + geography + math + science
    result = total_pages
    return result

print(solution())