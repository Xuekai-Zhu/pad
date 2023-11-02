def solution():
    """Micah bought envelopes to send, and depending on the weight of the envelope he will need more stamps. If an envelope weighs more than 5 pounds, he will need 5 stamps. If it weighs less than that, it will only need 2 stamps. If he bought 52 stamps with 6 envelopes that weigh less than 5 pounds, how many envelopes in total did Micah need to buy?"""
    # Define the total number of stamps Micah bought
    total_stamps = 52

    # Define the number of envelopes that weigh less than 5 pounds
    less_than_5 = 6

    # Calculate the number of stamps needed for each envelope that weighs more than 5 pounds
    stamps_per_heavy_envelope = 5

    # Calculate the number of stamps needed for each envelope that weighs less than 5 pounds
    stamps_per_light_envelope = 2

    # Calculate the total number of stamps needed for all envelopes
    total_stamps_needed = less_than_5 * stamps_per_light_envelope + (total_stamps - less_than_5 * stamps_per_light_envelope) / stamps_per_heavy_envelope * stamps_per_heavy_envelope

    # Calculate the total number of envelopes needed
    total_envelopes = less_than_5 + (total_stamps - less_than_5 * stamps_per_light_envelope) / stamps_per_heavy_envelope

    # return the result
    result = round(total_envelopes)
    return result

print(solution())