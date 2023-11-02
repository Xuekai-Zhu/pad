def solution():
    """This week, the fishmonger sold 50 kg of salmon. He sold three times more the following week. What was the total amount of fish sold in two weeks?"""
    week_one_salmon = 50
    week_two_salmon = week_one_salmon * 3
    total_salmon = week_one_salmon + week_two_salmon
    result = total_salmon
    return result

print(solution())