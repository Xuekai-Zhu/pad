def solution():
    """Jason goes to the library 4 times more often than William goes. If William goes 2 times per week to the library, how many times does Jason go to the library in 4 weeks?"""
    william_freq = 2
    jason_freq = 4 * william_freq
    total_jason_visits = jason_freq * 4
    result = total_jason_visits
    return result

print(solution())