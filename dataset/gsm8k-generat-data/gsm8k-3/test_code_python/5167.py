def solution():
    """Malcolm works in a company where they normally pack 40 apples in a box, producing 50 full boxes per day. Operations went as normal in one week. But in the next week, they packed 500 fewer apples per day. What's the total number of apples packed in the two weeks?"""
    # Define the number of apples in a box and boxes produced per day
    APPLES_PER_BOX = 40
    BOXES_PER_DAY = 50

    # Calculate the number of apples produced per day in the first week
    apples_per_day_week1 = APPLES_PER_BOX * BOXES_PER_DAY

    # Calculate the total number of apples produced in the first week
    total_apples_week1 = apples_per_day_week1 * 7

    # Calculate the number of apples produced per day in the second week
    apples_per_day_week2 = (APPLES_PER_BOX * (BOXES_PER_DAY - 500))

    # Calculate the total number of apples produced in the second week
    total_apples_week2 = apples_per_day_week2 * 7

    # Calculate the total number of apples produced in the two weeks
    total_apples = total_apples_week1 + total_apples_week2

    # Display the total number of apples produced
    result = total_apples
    return result

print(solution())