def solution():
    num_buckets = 8
    crabs_per_bucket = 12
    price_per_crab = 5
    days_per_week = 7

    # Calculate the total number of crabs Tom catches per day
    total_crabs_per_day = num_buckets * crabs_per_bucket

    # Calculate the total amount of money Tom makes per day
    total_money_per_day = total_crabs_per_day * price_per_crab

    # Calculate the total amount of money Tom makes per week
    total_money_per_week = total_money_per_day * days_per_week
    result = total_money_per_week
    return result

print(solution())