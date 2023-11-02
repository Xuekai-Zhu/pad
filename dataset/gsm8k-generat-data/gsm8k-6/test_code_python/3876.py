def solution():
    # Calculate the total amount of ground beef sold
    total_sold = 210 + (2 * 210) + 130 + (0.5 * 130)  # amount sold on Thursday and Friday, Saturday and Sunday

    # Calculate the amount of meat sold beyond their original plans
    beyond_plan = total_sold - 500

    result = beyond_plan
    return result

print(solution())