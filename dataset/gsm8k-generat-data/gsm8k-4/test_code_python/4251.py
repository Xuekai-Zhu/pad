def solution():
    """Carly is trying to get in shape to try out for the soccer team. She starts by running 2 miles a week. The second week, she runs twice as long plus 3 extra miles per week. The third week she runs 9/7 as much as she ran the second week. The week after that, she sprains her ankle and has to reduce her running time by 5 miles per week. How many miles did she run the week she was injured?"""
    # Define the initial running distance
    initial_distance = 2

    # Define the running distance for week 2
    week2_distance = (initial_distance * 2) + 3

    # Define the running distance for week 3
    week3_distance = (9 / 7) * week2_distance

    # Define the running distance for week 4
    week4_distance = week3_distance - 5

    result = week4_distance
    return result

print(solution())