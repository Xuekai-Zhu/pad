def solution():
    """An online newspaper had listed 100 visitors in October. The number of visitors in November increased by 15%. There were 15 more visitors in December than in November. What is the total number of visitors for these three months?"""
    # Define the number of visitors in October
    oct_visitors = 100

    # Calculate the number of visitors in November
    nov_visitors = oct_visitors * 1.15

    # Calculate the number of visitors in December
    dec_visitors = nov_visitors + 15

    # Calculate the total number of visitors for the three months
    total_visitors = oct_visitors + nov_visitors + dec_visitors

    # return the result
    result = total_visitors
    return result

print(solution())