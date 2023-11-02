def solution():
    num_bags_20 = 4
    num_apples_20 = 20

    num_bags_25 = 6
    num_apples_25 = 25

    num_apples_sold = 200

    # Calculate the total number of apples Ella had before selling any
    total_apples = (num_bags_20 * num_apples_20) + (num_bags_25 * num_apples_25)

    # Calculate the total number of apples Ella has left after selling 200
    num_apples_left = total_apples - num_apples_sold
    result = num_apples_left
    return result

print(solution())