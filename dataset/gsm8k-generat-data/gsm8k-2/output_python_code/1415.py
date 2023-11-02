def solution():
    """The company's data entry team had 5 employees working on a large project. Rudy types 64 words per minute, Joyce types 76 words per minute, Gladys types 91 words per minute, Lisa types 80 words per minute and Mike types 89 words per minute. What is the team's average typed words per minute?"""
    rudy_wpm = 64
    joyce_wpm = 76
    gladys_wpm = 91
    lisa_wpm = 80
    mike_wpm = 89
    total_wpm = rudy_wpm + joyce_wpm + gladys_wpm + lisa_wpm + mike_wpm
    average_wpm = total_wpm / 5
    result = average_wpm
    return result

print(solution())