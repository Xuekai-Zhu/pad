def solution():
    # Define the initial variables
    num_carpenters = 8
    num_chairs = 50
    num_days = 10

    # Calculate the rate of chair production
    chair_rate = num_chairs / (num_carpenters * num_days)

    # Calculate the number of carpenters needed to make 75 chairs in 10 days
    num_chairs_new = 75
    num_carpenters_new = round(num_chairs_new / (chair_rate * num_days))

    result = num_carpenters_new
    return result

print(solution())