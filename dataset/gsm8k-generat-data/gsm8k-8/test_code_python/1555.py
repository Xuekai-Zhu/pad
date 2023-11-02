def solution():
    # Define the number of gold stickers
    gold_stickers = 50

    # Calculate the number of silver stickers
    silver_stickers = 2 * gold_stickers

    # Calculate the number of bronze stickers
    bronze_stickers = silver_stickers - 20

    # Calculate the total number of stickers
    total_stickers = gold_stickers + silver_stickers + bronze_stickers

    # Calculate the number of stickers each student will receive
    stickers_per_student = total_stickers / 5
    result = stickers_per_student
    return result

print(solution())