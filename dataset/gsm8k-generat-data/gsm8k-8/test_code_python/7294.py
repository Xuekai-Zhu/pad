def solution():
    # Calculate the total number of stamps needed for the light envelopes
    light_envelopes_stamps = 6 * 2

    # Calculate the number of stamps needed for the heavy envelopes
    heavy_envelopes_stamps = 52 - light_envelopes_stamps

    # Calculate the number of heavy envelopes
    heavy_envelopes = heavy_envelopes_stamps / 5

    # Calculate the total number of envelopes
    total_envelopes = light_envelopes + heavy_envelopes
    result = total_envelopes
    return result

print(solution())