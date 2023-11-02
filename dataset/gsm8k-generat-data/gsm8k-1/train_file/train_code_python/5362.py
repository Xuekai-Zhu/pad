def solution():
    """Sandy's goal is to drink 3 liters of water in a day. She drinks 500 milliliters of water every after 2 hours. After how many hours will she be able to drink a total of 3 liters of water?"""
    goal = 3000  # 3 liters = 3000 ml
    interval = 2  # time interval in hours
    intake_per_interval = 500  # in ml
    total_intakes = goal / intake_per_interval  # number of intakes required
    total_time = interval * total_intakes  # time in hours
    result = total_time
    return result

print(solution())