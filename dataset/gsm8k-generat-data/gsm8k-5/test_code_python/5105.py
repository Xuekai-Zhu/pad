def solution():
    logs_per_pine_tree = 80  # Each pine tree makes 80 logs
    logs_per_maple_tree = 60  # Each maple tree makes 60 logs
    logs_per_walnut_tree = 100  # Each walnut tree makes 100 logs

    # Calculate the total number of logs Jerry gets
    total_logs = (logs_per_pine_tree * 8) + (logs_per_maple_tree * 3) + (logs_per_walnut_tree * 4)
    result = total_logs
    return result

print(solution())