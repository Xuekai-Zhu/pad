def solution():
    # Find the total number of rocks collected by Sydney and Conner after three days
    sydney_rocks = 837 + 4 + 2*(8*4) # Sydney collects 4 rocks on day one and twice as many as Conner on day three
    conner_rocks = 723 + 8*4 + 123  # Conner collects 8 times as many as Sydney on day one and 123 on day two
    rocks_needed = sydney_rocks - conner_rocks + 1  # Add 1 to Conner's total to tie with Sydney
    result = rocks_needed
    return result

print(solution())