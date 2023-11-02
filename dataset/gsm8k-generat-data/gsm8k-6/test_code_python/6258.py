def solution():
    # Calculate the total number of listens by the end of the year
    listens_per_month = 60000 / 3  # average number of listens per month
    total_listens = (2**2) * listens_per_month  # double the number of listens per month for 3 months
    result = total_listens
    return result

print(solution())