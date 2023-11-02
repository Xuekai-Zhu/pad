def solution():
    """An online newspaper had listed 100 visitors in October. The number of visitors in November increased by 15%. There were 15 more visitors in December than in November. What is the total number of visitors for these three months?"""
    # Define the number of visitors in October
    visitors_oct = 100

    # Calculate the number of visitors in November
    visitors_nov = int(visitors_oct * 1.15)

    # Calculate the number of visitors in December
    visitors_dec = visitors_nov + 15

    # Calculate the total number of visitors for the three months
    total_visitors = visitors_oct + visitors_nov + visitors_dec

    # Display the total number of visitors
    result = total_visitors
    return result

print(solution())