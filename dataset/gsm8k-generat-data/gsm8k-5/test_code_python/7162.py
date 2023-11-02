def solution():
    initial_feathers = 5263  # The chicken had 5263 feathers before the road crossings
    cars_dodged_first_time = 23  # The chicken dodged 23 cars the first time
    feathers_pulled_second_time = 2 * cars_dodged_first_time  # The person pulled out twice as many feathers as the cars dodged in the second crossing
    remaining_feathers = initial_feathers - feathers_pulled_second_time  # Calculate the feathers remaining after the second crossing
    result = remaining_feathers
    return result

print(solution())