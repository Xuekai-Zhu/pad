def solution():
    # Define the ratio of cartoon time to chore time
    cartoon_to_chore_ratio = 10/8

    # Convert 2 hours of cartoon time to minutes
    cartoon_time = 2 * 60

    # Calculate the total chore time
    total_chore_time = (cartoon_time * cartoon_to_chore_ratio) - cartoon_time

    result = total_chore_time
    return result

print(solution())