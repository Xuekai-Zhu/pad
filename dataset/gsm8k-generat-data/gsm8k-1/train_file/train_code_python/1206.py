def solution():
    """Nala found 5 seashells at the beach. The next day, she found another 7, and the following day, she found twice the number she got from the first two days. How many seashells does Nala have?"""
    day_one = 5
    day_two = 7
    day_three = 2*(day_one + day_two)
    total_seashells = day_one + day_two + day_three
    result = total_seashells
    return result

print(solution())