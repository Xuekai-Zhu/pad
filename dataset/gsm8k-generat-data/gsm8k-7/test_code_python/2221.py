def solution():
    july_earnings = 150
    august_earnings = 3 * july_earnings
    september_earnings = 2 * august_earnings

    # Calculate the total earnings over the three months
    total_earnings = july_earnings + august_earnings + september_earnings
    result = total_earnings
    return result

print(solution())