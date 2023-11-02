def solution():
    # Calculate the total waiting time
    total_waiting_time = 3 + 13 + 14 + 18  # in minutes

    # Calculate the total shopping time
    total_shopping_time = 90  # in minutes

    # Calculate the time spent shopping instead of waiting
    time_spent_shopping = total_shopping_time - total_waiting_time

    result = time_spent_shopping
    return result

print(solution())