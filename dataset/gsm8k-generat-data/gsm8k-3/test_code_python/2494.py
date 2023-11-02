def solution():
    """Sydney and Conner are having a three day rock collecting contest to see who can have the largest collection after adding to their existing collections. Before they start, Sydney has 837 rocks and Conner has 723. On day one, Sydney collects 4 rocks and Conner collects 8 times as many. On day two Sydney rests and Conner collects 123. On the third day, Sydney collects twice as many as Conner did on the first day. How many does Conner have to collect on day three to make sure he at least ties Sydney?"""
    # Define Sydney's and Conner's initial rock collections
    sydney_rocks = 837
    conner_rocks = 723

    # Define the number of rocks each collected on Day 1
    sydney_day1 = 4
    conner_day1 = 8 * sydney_day1

    # Define the number of rocks each collected on Day 2
    sydney_day2 = 0
    conner_day2 = 123

    # Define the number of rocks each collected on Day 3
    sydney_day3 = 2 * conner_day1
    conner_day3 = (sydney_rocks + sydney_day1 + sydney_day2 + sydney_day3) - conner_rocks

    # Display the number of rocks Conner needs to collect on Day 3 to tie Sydney
    result = conner_day3
    return result

print(solution())