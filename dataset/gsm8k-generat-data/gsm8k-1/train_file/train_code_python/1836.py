def solution():
    """Mr. Langsley commutes to work every day by bus. The bus picks him up at 6:00 a.m. and takes forty minutes to arrive at the first station. If Mr. Langsley arrives at work at 9:00 a.m., what's the total time taken in minutes from the first station to Mr. Langsley's workplace?"""
    total_time = (9 * 60) - ((6 * 60) + 40)
    result = total_time
    return result

print(solution())