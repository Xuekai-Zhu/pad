def solution():
    # Calculate the total time spent waiting
    total_waiting_time = 3 + 13 + 14 + 18

    # Convert the shopping time to minutes
    shopping_time = 1.5 * 60

    # Calculate the total time spent shopping
    total_shopping_time = shopping_time - total_waiting_time

    result = total_shopping_time
    return result

print(solution())