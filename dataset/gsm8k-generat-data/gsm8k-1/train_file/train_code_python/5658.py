def solution():
    """An online newspaper had listed 100 visitors in October. The number of visitors in November increased by 15%. There were 15 more visitors in December than in November. What is the total number of visitors for these three months?"""
    oct_visitors = 100
    nov_increase = 15
    nov_visitors = oct_visitors + (oct_visitors * (nov_increase / 100))
    dec_visitors = nov_visitors + 15
    total_visitors = oct_visitors + nov_visitors + dec_visitors
    result = total_visitors
    return result

print(solution())