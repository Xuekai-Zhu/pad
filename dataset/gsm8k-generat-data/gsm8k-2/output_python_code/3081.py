def solution():
    """Mimi picked up 2 dozen seashells on the beach. Kyle found twice as many shells as Mimi and put them in his pocket. Leigh grabbed one-third of the shells that Kyle found. How many seashells did Leigh have?"""
    mimi_shells = 2 * 12
    kyle_shells = 2 * mimi_shells
    leigh_shells = kyle_shells / 3
    result = leigh_shells
    return result

print(solution())