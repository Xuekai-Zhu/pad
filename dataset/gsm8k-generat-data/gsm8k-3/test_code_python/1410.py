def solution():
    """Brittney can chop 15 onions in 5 minutes. Carl can chop 20 onions within that same time. How many more onions can Carl chop in 30 minutes than Brittney?"""
    # Calculate the rate at which Brittney chops onions
    brittney_rate = 15 / 5

    # Calculate the number of onions Brittney can chop in 30 minutes
    brittney_onions = brittney_rate * 30

    # Calculate the rate at which Carl chops onions
    carl_rate = 20 / 5

    # Calculate the number of onions Carl can chop in 30 minutes
    carl_onions = carl_rate * 30

    # Calculate the difference in the number of onions Carl and Brittney can chop
    difference = carl_onions - brittney_onions

    # Display the difference in onions chopped
    result = difference
    return result

print(solution())