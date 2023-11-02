def solution():
    lollipops_per_store_trip = 1  # Felicity gets one lollipop every time she goes to the store
    sticks_per_lollipop = 10  # Felicity uses 10 sticks to build her fort from every lollipop
    sticks_required = 400  # Felicity needs 400 sticks to finish the fort
    completion_percentage = 0.6  # The fort is 60% complete

    # Calculate the total number of lollipops Felicity needs to finish the fort
    total_lollipops = sticks_required / sticks_per_lollipop

    # Calculate the number of lollipops Felicity has collected so far
    collected_lollipops = total_lollipops * completion_percentage

    # Calculate the number of weeks Felicity has been collecting lollipops for
    weeks_collected = collected_lollipops / (lollipops_per_store_trip * 3)

    result = weeks_collected
    return result

print(solution())