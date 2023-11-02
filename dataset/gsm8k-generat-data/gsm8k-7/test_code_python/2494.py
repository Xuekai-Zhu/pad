def solution():
    sydney_collection = 837
    conner_collection = 723

    # Day 1: Sydney collects 4 rocks, Conner collects 8 times as many
    sydney_collection += 4
    conner_collection += 4 * 8

    # Day 2: Sydney rests, Conner collects 123 rocks
    conner_collection += 123

    # Day 3: Sydney collects twice as many as Conner did on Day 1
    conner_day1_collection = 4 * 8
    sydney_day3_collection = 2 * conner_day1_collection
    conner_collection_needed = sydney_day3_collection - conner_collection

    result = conner_collection_needed
    return result

print(solution())