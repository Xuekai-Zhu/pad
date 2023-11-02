def solution():
    """Jame gets 20 singing lessons.  He gets the first lesson free and after the first 10 paid lessons he only needs to pay for every other lesson.  Each lesson is $5.  His uncle pays for half.  How much does James pay?"""
    
    # Define the cost per lesson and the number of free lessons
    LESSON_COST = 5
    FREE_LESSONS = 1
    
    # Calculate the number of paid lessons
    paid_lessons = 20 - FREE_LESSONS
    
    # Calculate the cost of the first 10 paid lessons
    first_10_cost = 10 * LESSON_COST
    
    # Calculate the cost of the remaining paid lessons
    remaining_lessons = paid_lessons - 10
    remaining_cost = remaining_lessons // 2 * LESSON_COST
    
    # Calculate the total cost and James' share
    total_cost = first_10_cost + remaining_cost
    james_share = total_cost / 2
    
    # Display James' share
    result = james_share
    return result

print(solution())