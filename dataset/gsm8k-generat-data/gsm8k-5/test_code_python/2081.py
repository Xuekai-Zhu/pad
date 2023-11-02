def solution():
    num_low_grades = 4  # Cassidy got four grades below a B
    base_grounding = 14  # Cassidy is grounded for 14 days
    extra_days = 3  # Cassidy gets an additional 3 days grounded for each low grade

    # Calculate the total grounding time
    total_grounding = base_grounding + (num_low_grades * extra_days)
    result = total_grounding
    return result

print(solution())