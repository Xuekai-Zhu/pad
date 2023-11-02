def solution():
    feathers_per_flamingo = 20
    pluck_percentage = 0.25
    num_boas = 12
    feathers_per_boa = 200

    # Calculate the total number of feathers needed
    total_feathers = num_boas * feathers_per_boa

    # Calculate the total number of feathers that can be safely plucked from one flamingo
    safe_feathers_per_flamingo = feathers_per_flamingo * pluck_percentage

    # Calculate the number of flamingos needed
    num_flamingos = total_feathers / safe_feathers_per_flamingo
    result = num_flamingos
    return result

print(solution())