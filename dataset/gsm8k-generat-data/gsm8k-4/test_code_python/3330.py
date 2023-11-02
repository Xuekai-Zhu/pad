def solution():
    """Jane bought pens for her three students. Each student received 62 red pens and 43 black pens. They pooled their pens together and took them from the pool whenever they needed them. After the first month, they had taken a total of 37 pens from the pool. After the second month, they had taken another 41 pens from the pool. Then Jane decided to split the remaining pens equally among them. How many pens will each student get now?"""
    # Define the number of students and the number of red/black pens each student received
    num_students = 3
    red_pens_per_student = 62
    black_pens_per_student = 43

    # Calculate the total number of pens each student received
    total_pens_per_student = red_pens_per_student + black_pens_per_student

    # Calculate the number of pens they took from the pool in the first two months
    pens_taken = 37 + 41

    # Calculate the total number of pens they had in the pool
    total_pens = (total_pens_per_student * num_students) - pens_taken

    # Calculate the number of pens each student will get now
    pens_per_student = total_pens // num_students

    # Return the result
    result = pens_per_student
    return result

print(solution())