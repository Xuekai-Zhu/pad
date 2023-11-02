def solution():
    """A special school for deaf and blind students has a deaf student population three times the size of blind student population. If the number of deaf students is 180, how many students are there altogether?"""
    deaf_population = 180
    blind_population = deaf_population / 3
    total_population = deaf_population + blind_population
    result = total_population
    return result

print(solution())