def solution():
    """Maryann spends seven times as long doing accounting as calling clients. If she worked 560 minutes today, how many minutes did she spend calling clients?"""
    # Define the ratio of accounting time to calling time
    ratio = 7

    # Calculate the total amount of time worked by Maryann
    total_time = 560

    # Calculate the total time spent on accounting
    accounting_time = total_time / (1 + ratio)

    # Calculate the total time spent calling clients
    calling_time = accounting_time * ratio

    # Display the time spent calling clients
    result = calling_time
    return result

print(solution())