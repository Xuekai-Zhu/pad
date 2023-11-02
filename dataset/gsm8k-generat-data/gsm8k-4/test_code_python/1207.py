def solution():
    """Nala found 5 seashells at the beach. The next day, she found another 7, and the following day, she found twice the number she got from the first two days. How many seashells does Nala have?"""
    # Define the number of seashells found each day
    day1 = 5
    day2 = 7
    day3 = (day1 + day2) * 2

    # Calculate the total number of seashells
    total_seashells = day1 + day2 + day3

    # return the result
    result = total_seashells
    return result

print(solution())