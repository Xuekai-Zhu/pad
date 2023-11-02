def solution():
    """Sydney and Conner are having a three day rock collecting contest to see who can have the largest collection after adding to their existing collections. Before they start, Sydney has 837 rocks and Conner has 723. On day one, Sydney collects 4 rocks and Conner collects 8 times as many. On day two Sydney rests and Conner collects 123. On the third day, Sydney collects twice as many as Conner did on the first day. How many does Conner have to collect on day three to make sure he at least ties Sydney?"""
    # Define Sydney and Conner's initial number of rocks
    sydney_rocks = 837
    conner_rocks = 723

    # Define the number of rocks collected on each day
    sydney_day1 = 4
    conner_day1 = sydney_day1 * 8
    conner_day2 = 123
    sydney_day3 = conner_day1 * 2

    # Calculate each person's total number of rocks
    sydney_total = sydney_rocks + sydney_day1 + sydney_day3
    conner_total = conner_rocks + conner_day1 + conner_day2

    # Calculate how many more rocks Conner needs to collect on day three to tie Sydney
    rocks_needed = sydney_total - conner_total + 1

    result = rocks_needed
    return result

print(solution())