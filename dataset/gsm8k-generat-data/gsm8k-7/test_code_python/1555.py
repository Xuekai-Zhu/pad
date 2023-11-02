def solution():
    num_gold_stickers = 50
    num_silver_stickers = num_gold_stickers * 2
    num_bronze_stickers = num_silver_stickers - 20
    num_students = 5

    # Calculate the total number of stickers that Miss Walter has
    total_stickers = num_gold_stickers + num_silver_stickers + num_bronze_stickers

    # Calculate the number of stickers each student will receive
    num_stickers_per_student = total_stickers / num_students
    result = num_stickers_per_student
    return result

print(solution())