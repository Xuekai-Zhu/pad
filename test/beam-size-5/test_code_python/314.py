def solution():
    boys = 30  # The classroom has 30 boys
    girls = 3 * boys  # The classroom has 3 times as many girls as they do boys
    nongendered_children = boys / 10  # The classroom has 1/10 as many nongendered children as they do boys

    # Calculate the total number of children
    total_children = boys + girls + nongendered_children
    result = total_children
    return result

print(solution())