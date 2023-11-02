def solution():
    """Charlie is a tennis pro. He spends most of the day teaching others lessons on how to improve their game. His standard fee is $80 per hour for lessons, but he reduces his rate by 25% when he is giving lessons to a veteran. If today Charlie has 4 1-hour lessons at his standard rate and 2 1-hour lessons with a veteran, what is the total amount of money he will make for the day, in dollars?"""
    standard_rate = 80
    veteran_rate = standard_rate * 0.75
    standard_lessons = 4
    veteran_lessons = 2
    standard_earnings = standard_rate * standard_lessons
    veteran_earnings = veteran_rate * veteran_lessons
    total_earnings = standard_earnings + veteran_earnings

    result = total_earnings
    return result

print(solution())