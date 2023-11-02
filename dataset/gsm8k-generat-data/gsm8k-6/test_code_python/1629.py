def solution():
    # Calculate the total number of visitors in one day
    total_visitors = 50 * 8  # 50 new visitors every hour, zoo open for 8 hours
    gorilla_visitors = 0.8 * total_visitors  # 80% of visitors go to gorilla exhibit
    result = gorilla_visitors
    return result

print(solution())