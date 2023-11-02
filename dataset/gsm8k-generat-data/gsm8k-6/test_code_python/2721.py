def solution():
    # Calculate the total number of lollipops Felicity has collected
    sticks_per_lollipop = 1  # she gets a lollipop every time she goes to the store
    sticks_needed = 400  # the fort needs 400 sticks to finish it
    lollipops_needed = sticks_needed / sticks_per_lollipop  # calculate the number of lollipops needed to build the fort
    lollipops_collected = lollipops_needed / 0.6  # if the fort is 60% complete, she has collected 100% of the sticks needed
    weeks_collected = lollipops_collected / 3  # her family goes to the store three times a week
    result = weeks_collected
    return result

print(solution())