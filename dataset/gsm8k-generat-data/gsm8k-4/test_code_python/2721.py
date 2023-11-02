def solution():
    """Every time she goes to the store, Felicity gets a lollipop. After she finishes them, she uses the sticks to build a fort. The fort needs 400 sticks to finish it. Her family goes to the store three times a week and she always goes. If the fort is 60% complete, how many weeks has Felicity been collecting lollipops for?"""
    # Define the total number of sticks needed to complete the fort
    TOTAL_STICKS = 400

    # Define the number of sticks Felicity gets with each lollipop
    STICKS_PER_LOLLIPOP = 1

    # Define the number of times Felicity goes to the store each week
    STORE_VISITS_PER_WEEK = 3

    # Calculate the number of sticks Felicity gets each week
    sticks_per_week = STICKS_PER_LOLLIPOP * STORE_VISITS_PER_WEEK

    # Calculate the total number of weeks needed to collect enough sticks for the fort
    total_weeks = TOTAL_STICKS / sticks_per_week

    # Calculate the number of weeks Felicity has been collecting lollipops for based on the fort's 60% completion
    weeks_since_start = total_weeks * 0.6

    # Return the result
    result = weeks_since_start
    return result

print(solution())