def solution():
    num_students = 8
    num_paper_per_student = 3
    num_glue_bottles = 6
    num_dropped = (num_students * num_paper_per_student + num_glue_bottles) / 2
    num_paper_left = 5
    num_glue_left = num_glue_bottles / 2

    # Calculate the total number of supplies left
    total_supplies_left = num_paper_left + num_glue_left

    result = total_supplies_left
    return result

print(solution())