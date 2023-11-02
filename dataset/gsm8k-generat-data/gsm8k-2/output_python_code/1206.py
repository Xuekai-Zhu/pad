def solution():
    """Nala found 5 seashells at the beach. The next day, she found another 7, and the following day, she found twice the number she got from the first two days. How many seashells does Nala have?"""
    first_day = 5
    second_day = 7
    third_day = 2 * (first_day + second_day)
    total_seashells = first_day + second_day + third_day
    result = total_seashells
    return result

print(solution())