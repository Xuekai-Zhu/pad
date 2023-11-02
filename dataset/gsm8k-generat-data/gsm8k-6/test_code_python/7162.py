def solution():
    # Calculate the number of feathers pulled out by the person
    feathers_pulled_out = 2 * 23  # the person pulled out twice as many feathers as the number of cars the chicken had dodged
    feathers_left = 5263 - (23 + feathers_pulled_out)  # calculate the number of feathers left after both crossings
    result = feathers_left
    return result

print(solution())