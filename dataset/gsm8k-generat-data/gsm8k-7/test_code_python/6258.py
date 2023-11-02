def solution():
    num_months_left = 3
    current_listens = 60000

    # Calculate the total number of listens by doubling the listens per month each month left
    total_listens = current_listens * (2 ** num_months_left)

    result = total_listens
    return result

print(solution())