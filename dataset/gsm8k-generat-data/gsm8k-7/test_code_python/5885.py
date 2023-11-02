def solution():
    first_hour_rate = 1/12 # one t-shirt every 12 minutes
    second_hour_rate = 1/6 # one t-shirt every 6 minutes

    # Calculate the number of t-shirts made in the first hour
    num_first_hour = first_hour_rate * 60 # 60 minutes in 1 hour

    # Calculate the number of t-shirts made in the second hour
    num_second_hour = second_hour_rate * 60 # 60 minutes in 1 hour

    # Calculate the total number of t-shirts made in two hours
    total_num = num_first_hour + num_second_hour
    result = total_num
    return result

print(solution())