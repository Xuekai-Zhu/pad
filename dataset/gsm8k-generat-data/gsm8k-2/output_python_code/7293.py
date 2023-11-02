def solution():
    """Micah bought envelopes to send, and depending on the weight of the envelope he will need more stamps. If an envelope weighs more than 5 pounds, he will need 5 stamps. If it weighs less than that, it will only need 2 stamps. If he bought 52 stamps with 6 envelopes that weigh less than 5 pounds, how many envelopes in total did Micah need to buy?"""
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