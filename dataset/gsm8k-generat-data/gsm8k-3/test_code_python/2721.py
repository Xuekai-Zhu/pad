def solution():
    """Every time she goes to the store, Felicity gets a lollipop. After she finishes them, she uses the sticks to build a fort. The fort needs 400 sticks to finish it. Her family goes to the store three times a week and she always goes. If the fort is 60% complete, how many weeks has Felicity been collecting lollipops for?"""
    # Calculate the number of sticks Felicity collects each week
    sticks_per_week = 3 * 1  # Felicity gets one stick per lollipop and goes to the store 3 times a week

    # Calculate the number of weeks it will take to collect 400 sticks
    total_weeks = 400 / sticks_per_week

    # Calculate the number of weeks Felicity has been collecting lollipops for based on the fort's completion percentage
    completed_weeks = total_weeks * 0.6

    # Display the number of weeks Felicity has been collecting lollipops for
    result = completed_weeks
    return result

print(solution())