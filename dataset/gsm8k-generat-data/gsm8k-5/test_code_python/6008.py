def solution():
    buckets_checked_per_day = 8  # Tom checks 8 crab buckets per day
    crabs_per_bucket = 12  # Each crab bucket contains 12 crabs
    crabs_sold_for = 5  # Tom sells each crab for $5
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of crabs Tom catches per week
    total_crabs = buckets_checked_per_day * crabs_per_bucket * days_per_week

    # Calculate the total amount of money Tom makes per week
    total_money = total_crabs * crabs_sold_for
    result = total_money
    return result

print(solution())