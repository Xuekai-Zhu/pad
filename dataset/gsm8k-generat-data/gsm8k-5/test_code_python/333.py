def solution():
    chocolates_per_week = 2 + 1  # Kantana buys 2 chocolates for herself and 1 for her sister every Saturday
    chocolates_bought_last_week = 2 + 1 + 10  # Kantana bought 2 chocolates for herself, 1 for her sister, and 10 as a birthday gift for her friend

    # Calculate the total number of chocolates Kantana bought in a month
    chocolates_per_month = chocolates_per_week * 4 + chocolates_bought_last_week

    result = chocolates_per_month
    return result

print(solution())