def solution():
    """Every time she goes to the store, Felicity gets a lollipop. After she finishes them, she uses the sticks to build a fort. The fort needs 400 sticks to finish it. Her family goes to the store three times a week and she always goes. If the fort is 60% complete, how many weeks has Felicity been collecting lollipops for?"""
    fort_sticks = 400
    lollipop_sticks = 1
    sticks_needed = fort_sticks / 0.6
    weeks = sticks_needed / (lollipop_sticks * 3)
    result = weeks
    return result

print(solution())