def solution():
    """Brittney can chop 15 onions in 5 minutes. Carl can chop 20 onions within that same time. How many more onions can Carl chop in 30 minutes than Brittney?"""
    # Calculate the rate of onion chopping for Brittney and Carl
    brittney_rate = 15 / 5
    carl_rate = 20 / 5

    # Calculate the number of onions each person can chop in 30 minutes
    brittney_onions = brittney_rate * 30
    carl_onions = carl_rate * 30

    # Calculate the difference in the number of onions each can chop
    difference = carl_onions - brittney_onions

    # return the result
    result = difference
    return result

print(solution())