def solution():
    stamps_for_heavy_envelopes = 5  # Micah needs 5 stamps for envelopes weighing over 5 pounds
    stamps_for_light_envelopes = 2  # Micah needs 2 stamps for envelopes weighing less than 5 pounds
    total_stamps = 52  # Micah bought a total of 52 stamps
    light_envelopes = 6  # Micah bought 6 envelopes weighing less than 5 pounds

    # Calculate the number of stamps used for the light envelopes
    stamps_for_light_envelopes_used = light_envelopes * stamps_for_light_envelopes

    # Calculate the total number of stamps used for all envelopes
    total_stamps_used = total_stamps - stamps_for_light_envelopes_used

    # Calculate the number of heavy envelopes Micah sent
    heavy_envelopes = total_stamps_used / stamps_for_heavy_envelopes
    result = light_envelopes + heavy_envelopes
    return result

print(solution())