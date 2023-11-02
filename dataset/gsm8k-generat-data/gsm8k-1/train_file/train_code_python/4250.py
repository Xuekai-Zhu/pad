def solution():
    """Carly is trying to get in shape to try out for the soccer team. She starts by running 2 miles a week. The second week, she runs twice as long plus 3 extra miles per week. The third week she runs 9/7 as much as she ran the second week. The week after that, she sprains her ankle and has to reduce her running time by 5 miles per week. How many miles did she run the week she was injured?"""
    first_week = 2
    second_week = 2 * 2 + 3
    third_week = (9/7) * second_week
    fourth_week = third_week - 5
    injured_week = fourth_week
    result = injured_week
    return result

print(solution())