def solution():
    """A special school for deaf and blind students has a deaf student population three times the size of blind student population. If the number of deaf students is 180, how many students are there altogether?"""
    deaf_pop = 180
    blind_pop = deaf_pop / 3
    total_pop = deaf_pop + blind_pop
    result = total_pop
    return result

print(solution())