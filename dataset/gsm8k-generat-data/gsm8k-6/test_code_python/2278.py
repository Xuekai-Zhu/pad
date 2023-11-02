def solution():
    # Calculate the number of 30-minute walks Johnny will take
    num_30_min_walks = (4*60) / 30  # Johnny works for 4 hours = 240 minutes. Each 30-minute walk takes up 30 minutes.

    # Calculate the number of 60-minute walks Johnny will take
    num_60_min_walks = 6

    # Calculate the total number of dogs Johnny will walk
    total_dogs = num_30_min_walks * 3 + num_60_min_walks * 1

    # Calculate the total amount of money Johnny will make in a day
    total_money_per_day = (num_30_min_walks * 15 + num_60_min_walks * 20) / 2  # to get the average hourly rate

    # Calculate the total amount of money Johnny will make in a week
    total_money_per_week = total_money_per_day * 5  # Johnny works for 5 days a week

    result = total_money_per_week
    return result

print(solution())