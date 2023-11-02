def solution():
    """Heath spent his weekend helping at his uncle’s farm planting carrots. He planted 400 rows of carrots with 300 plants in each row. He used a machine to get the planting done and it took him 20 hours. How many carrots did he plant each hour?"""
    # Define the total number of carrots planted
    total_carrots = 400 * 300

    # Define the number of hours spent planting
    hours_spent = 20

    # Calculate the number of carrots planted per hour
    carrots_per_hour = total_carrots / hours_spent

    # Return the result
    result = carrots_per_hour
    return result

print(solution())