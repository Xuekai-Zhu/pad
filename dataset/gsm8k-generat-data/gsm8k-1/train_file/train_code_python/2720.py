def solution():
    """ Every time she goes to the store, Felicity gets a lollipop. After she finishes them, she uses the sticks to build a fort. The fort needs 400 sticks to finish it. Her family goes to the store three times a week and she always goes. If the fort is 60% complete, how many weeks has Felicity been collecting lollipops for? """
    sticks_per_lollipop = 1
    sticks_needed = 400
    num_lollipops_needed = sticks_needed / sticks_per_lollipop
    lollipops_per_week = 3
    weeks_to_collect = num_lollipops_needed / lollipops_per_week
    fort_completion = 0.6
    weeks_building_fort = weeks_to_collect * fort_completion
    result = weeks_building_fort
    return result

print(solution())