def solution():
    # Calculate the number of toy cars Jerome bought this month
    bought_this_month = 40 - 5  # he has 40 toy cars now and bought 5 last month
    # Calculate the number of toy cars Jerome had originally
    originally = (bought_this_month/2) + 5  # he bought twice as many this month as last month
    result = originally
    return result

print(solution())