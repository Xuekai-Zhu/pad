def solution():
    """Ruby is taking dance lessons. They cost $75 for 10 classes in one pack. She can add additional classes at the price of 1/3 more than the average price of a class on the lesson in the pack. if she takes 13 total classes, how much does she pay?"""
    # Define the cost of the lesson pack and the number of lessons in the pack
    PACK_COST = 75
    PACK_LESSONS = 10

    # Define the total number of lessons Ruby takes
    total_lessons = 13

    # Calculate the average price of a lesson in the pack
    pack_price_per_lesson = PACK_COST / PACK_LESSONS

    # Calculate the cost of the additional lessons
    additional_lessons = total_lessons - PACK_LESSONS
    additional_price_per_lesson = pack_price_per_lesson * (1 + 1/3)
    additional_lesson_cost = additional_lessons * additional_price_per_lesson

    # Calculate the total cost of all the lessons
    total_cost = PACK_COST + additional_lesson_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())