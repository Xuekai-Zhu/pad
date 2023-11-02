def solution():
    # Calculate the number of guests initially invited
    initial_guests = 3*12  # 3 dozen guests

    # Calculate the number of guests bringing a plus one
    plus_ones = (1/3) * initial_guests

    # Calculate the number of guests who can't make it
    cancellations = 5

    # Calculate the total number of chairs needed, adding 12 extra
    total_chairs = initial_guests + plus_ones - cancellations + 12
    result = total_chairs
    return result

print(solution())