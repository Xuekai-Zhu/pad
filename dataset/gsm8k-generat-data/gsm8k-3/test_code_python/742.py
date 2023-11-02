def solution():
    """Brendan can cut 8 yards of grass per day, he bought a lawnmower and it helped him to cut more yards by Fifty percent per day. How many yards will Brendan be able to cut after a week?"""
    # Define the amount of yards Brendan can cut per day without the lawnmower
    yards_per_day = 8

    # Define the percentage increase in yards cut per day with the lawnmower
    increase_percentage = 50

    # Calculate the amount of yards Brendan can cut per day with the lawnmower
    yards_per_day_with_lawnmower = yards_per_day * (1 + increase_percentage/100)

    # Calculate the total amount of yards Brendan can cut after a week (7 days)
    total_yards_cut = yards_per_day_with_lawnmower * 7

    # Display the total yards cut
    result = total_yards_cut
    return result

print(solution())