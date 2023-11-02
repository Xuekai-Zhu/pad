def solution():
    # Calculate the total number of chocolates Kantana bought for the month
    chocolates_per_week = 2 + 1  # Kantana buys 2 chocolates for herself and 1 for her sister every Saturday
    chocolates_for_gift = 10  # Kantana bought 10 more chocolates as a gift for her friend
    total_chocolates = chocolates_per_week * 4 + chocolates_for_gift  # Kantana buys chocolates every Saturday for 4 weeks plus the gift
    result = total_chocolates
    return result

print(solution())