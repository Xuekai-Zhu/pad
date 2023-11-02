def solution():
    # Calculate the rate at which Brittney can chop onions
    brittney_rate = 15 / 5

    # Calculate the rate at which Carl can chop onions
    carl_rate = 20 / 5

    # Calculate the number of onions Brittney can chop in 30 minutes
    brittney_onions_30mins = brittney_rate * 30

    # Calculate the number of onions Carl can chop in 30 minutes
    carl_onions_30mins = carl_rate * 30

    # Calculate the difference in the number of onions Carl can chop compared to Brittney
    difference = carl_onions_30mins - brittney_onions_30mins

    result = difference
    return result

print(solution())