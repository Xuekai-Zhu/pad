def solution():
    weight_per_paper = 1/5  # each piece of paper weighs 1/5 of an ounce
    num_papers = 8  # Jessica used 8 pieces of paper
    weight_papers = weight_per_paper * num_papers  # total weight of the papers

    weight_envelope = 2/5  # the envelope weighs 2/5 of an ounce

    total_weight = weight_papers + weight_envelope  # total weight of the letter

    stamps_per_ounce = 1  # Jessica needs one stamp per ounce

    # Calculate the total number of stamps required
    total_stamps = total_weight / stamps_per_ounce
    result = total_stamps
    return result

print(solution())