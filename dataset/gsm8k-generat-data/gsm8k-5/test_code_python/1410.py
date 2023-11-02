def solution():
    # Calculate the rate at which each person chops onions
    brittney_rate = 15/5 # Brittney can chop 15 onions every 5 minutes
    carl_rate = 20/5 # Carl can chop 20 onions every 5 minutes

    # Calculate the number of onions each person can chop in 30 minutes
    brittney_onions = brittney_rate * 30 # Brittney can chop this many onions in 30 minutes
    carl_onions = carl_rate * 30 # Carl can chop this many onions in 30 minutes

    # Calculate the difference in the number of onions they can chop in 30 minutes
    difference = carl_onions - brittney_onions
    result = difference
    return result

print(solution())