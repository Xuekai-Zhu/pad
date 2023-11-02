def solution():
    
    stamps_for_light_envelope = 2
    stamps_for_heavy_envelope = 5
    light_envelopes = 6
    total_stamps = 52
    remaining_stamps = total_stamps - (light_envelopes * stamps_for_light_envelope)
    heavy_envelopes = remaining_stamps // stamps_for_heavy_envelope
    total_envelopes = light_envelopes + heavy_envelopes
    result = total_envelopes
    return result

print(solution())