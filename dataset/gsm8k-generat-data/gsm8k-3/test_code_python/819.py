def solution():
    """James decides to build a tin house by collecting 500 tins in a week. On the first day, he collects 50 tins. On the second day, he manages to collect 3 times that number. On the third day, he collects 50 tins fewer than the number he collected on the second day. If he collects an equal number of tins on the remaining days of the week, what's the number of tins he collected each day for the rest of the week?"""
    # Define the number of tins James collected on the first, second, and third day
    tins_day1 = 50
    tins_day2 = 3 * tins_day1
    tins_day3 = tins_day2 - 50

    # Calculate the total number of tins collected in the first three days
    total_tins = tins_day1 + tins_day2 + tins_day3

    # Calculate the remaining number of tins to collect in the week
    remaining_tins = 500 - total_tins

    # Calculate the number of tins James needs to collect each day for the rest of the week
    daily_tins = remaining_tins // 4

    # Display the number of tins James collected each day for the rest of the week
    result = daily_tins
    return result

print(solution())