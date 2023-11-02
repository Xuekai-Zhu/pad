def solution():
    # Calculate the total number of strawberries Hannah harvests in April
    total_strawberries = 5 * 30  # 5 strawberries daily for the 30 days in April
    remaining_strawberries = total_strawberries - 20 - 30  # Hannah gives away 20 strawberries and 30 strawberries are stolen
    result = remaining_strawberries
    return result

print(solution())