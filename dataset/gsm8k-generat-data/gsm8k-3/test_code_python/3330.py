def solution():
    """Jane bought pens for her three students. Each student received 62 red pens and 43 black pens. They pooled their pens together and took them from the pool whenever they needed them. After the first month, they had taken a total of 37 pens from the pool. After the second month, they had taken another 41 pens from the pool. Then Jane decided to split the remaining pens equally among them. How many pens will each student get now?"""
    # Define the initial number of pens each student had
    red_pens = 62
    black_pens = 43

    # Calculate the number of pens in the pool
    pool_pens = (red_pens + black_pens) * 3 - (37 + 41)

    # Calculate the number of pens each student will get after the pool is split equally
    pens_per_student = pool_pens / 3

    # Display the number of pens each student will get
    result = pens_per_student
    return result

print(solution())