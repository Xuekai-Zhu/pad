def solution():
    """Tammy has 10 orange trees from which she can pick 12 oranges each day. Tammy sells 6-packs of oranges for $2. How much money will Tammy have earned after 3 weeks if she sells all her oranges?"""
    # Define the number of orange trees and oranges per day
    num_trees = 10
    oranges_per_day = 12

    # Calculate the total number of oranges Tammy can pick in 3 weeks
    total_days = 7 * 3 # 3 weeks, 7 days per week
    total_oranges = num_trees * oranges_per_day * total_days

    # Calculate the number of 6-packs of oranges Tammy can sell
    num_six_packs = total_oranges // 6

    # Calculate the total earnings from selling the oranges
    total_earnings = num_six_packs * 2

    # Display the total earnings
    result = total_earnings
    return result

print(solution())