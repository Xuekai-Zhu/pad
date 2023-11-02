def solution():
    # Starting collections
    sydney_collection = 837
    conner_collection = 723

    # Day 1 collections
    sydney_day1 = sydney_collection + 4
    conner_day1 = conner_collection + (8 * 4)

    # Day 2 collections
    sydney_day2 = sydney_day1
    conner_day2 = conner_day1 + 123

    # Day 3 collections
    sydney_day3 = sydney_day2 + (2 * conner_day1) # Sydney collects twice as many as Conner did on day 1
    conner_day3 = (sydney_day3 - conner_collection) - (conner_day1 + conner_day2) # Conner has to collect at least this many to tie Sydney

    result = conner_day3
    return result

print(solution())