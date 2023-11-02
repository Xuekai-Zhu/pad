def solution():
    # Calculate how much Rick spent on lunch
    rick_spent = 45 * 2  # Rick spent twice as much as Jose

    # Calculate how much Adam spent on lunch
    adam_spent = (2/3) * rick_spent

    # Calculate the total cost of lunch
    total_spent = rick_spent + adam_spent + 45  # Add Jose's lunch

    result = total_spent
    return result

print(solution())