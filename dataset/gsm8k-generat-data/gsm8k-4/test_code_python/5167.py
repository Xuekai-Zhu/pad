def solution():
    """Malcolm works in a company where they normally pack 40 apples in a box, producing 50 full boxes per day. Operations went as normal in one week. But in the next week, they packed 500 fewer apples per day. What's the total number of apples packed in the two weeks?"""
    # Define the number of boxes produced per day in the first week
    boxes_per_day_week1 = 50

    # Define the number of apples per box
    apples_per_box = 40

    # Calculate the total number of apples packed in the first week
    total_apples_week1 = boxes_per_day_week1 * apples_per_box * 7

    # Define the number of boxes produced per day in the second week
    boxes_per_day_week2 = 50

    # Define the number of apples per box in the second week
    apples_per_box_week2 = 40 - (500/50)
    
    # Calculate the total number of apples packed in the second week
    total_apples_week2 = boxes_per_day_week2 * apples_per_box_week2 * 7

    # Calculate the total number of apples packed in two weeks
    total_apples = total_apples_week1 + total_apples_week2

    # return the result
    result = total_apples
    return result

print(solution())