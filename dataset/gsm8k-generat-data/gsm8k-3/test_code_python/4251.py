def solution():
    """Carly is trying to get in shape to try out for the soccer team. She starts by running 2 miles a week. The second week, she runs twice as long plus 3 extra miles per week. The third week she runs 9/7 as much as she ran the second week. The week after that, she sprains her ankle and has to reduce her running time by 5 miles per week. How many miles did she run the week she was injured?"""
    # Initialize the number of miles Carly runs each week
    week1 = 2
    week2 = (2 * 2) + 3
    week3 = (9/7) * week2
    week4 = week3 - 5

    # Determine how many miles Carly runs the week she was injured (week 4)
    miles_injured = week4

    # Display the number of miles Carly runs the week she was injured
    result = miles_injured
    return result

print(solution())