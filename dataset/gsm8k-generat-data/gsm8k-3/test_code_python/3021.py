def solution():
    """Jessica wrote a long letter to her aunt and needed to put stamps on it to mail it. She used eight pieces of paper that weigh 1/5 of an ounce each, and her envelope weighs 2/5 of an ounce. She needed one stamp per ounce. How many stamps did Jessica need to mail her letter?"""
    # Define the weight of one piece of paper and the weight of the envelope
    PAPER_WEIGHT = 1/5
    ENVELOPE_WEIGHT = 2/5

    # Calculate the total weight of the letter
    paper_total_weight = 8 * PAPER_WEIGHT
    total_weight = paper_total_weight + ENVELOPE_WEIGHT

    # Calculate the number of stamps needed
    stamps_needed = total_weight

    # Display the number of stamps needed
    result = stamps_needed
    return result

print(solution())