def solution():
    # Calculate the total number of candy bars Fred and Uncle Bob have
    total_candybars = 12 + (12 + 6)

    # Calculate the total number of candy bars Jacqueline has
    jacqueline_candybars = 10 * total_candybars

    # Calculate 40% of Jacqueline's candy bars
    forty_percent_jacqueline = 0.4 * jacqueline_candybars
    result = forty_percent_jacqueline
    return result

print(solution())