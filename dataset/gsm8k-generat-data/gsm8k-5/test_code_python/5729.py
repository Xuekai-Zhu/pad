def solution():
    feathers_per_boa = 200  # Each boa requires 200 feathers
    boas_to_make = 12  # Milly needs to make 12 boas
    total_feathers_needed = feathers_per_boa * boas_to_make  # Milly needs a total of 2400 feathers

    feathers_per_flamingo = 20  # Each flamingo has 20 tail feathers
    percent_of_feathers_safe_to_pluck = 0.25  # It's safe to pluck 25% of the feathers at one time

    # Calculate the number of flamingoes needed to harvest the required number of feathers
    feathers_per_flamingo_to_harvest = feathers_per_flamingo * percent_of_feathers_safe_to_pluck
    flamingoes_needed = total_feathers_needed / feathers_per_flamingo_to_harvest
    result = flamingoes_needed
    return result

print(solution())