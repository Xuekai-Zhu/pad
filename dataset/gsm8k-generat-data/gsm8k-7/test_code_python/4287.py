def solution():
    starting_parsley = 25
    whole_plates = 8
    half_plates = 12
    total_half_plugs = half_plates / 2  # Convert half plates to half sprigs

    # Calculate the total number of sprigs used
    total_used = whole_plates + total_half_plugs

    # Calculate the remaining number of sprigs
    remaining_sprigs = starting_parsley - total_used
    result = remaining_sprigs
    return result

print(solution())