def solution():
    """Jessica wrote a long letter to her aunt and needed to put stamps on it to mail it. She used eight pieces of paper that weigh 1/5 of an ounce each, and her envelope weighs 2/5 of an ounce. She needed one stamp per ounce. How many stamps did Jessica need to mail her letter?"""
    paper_weight = 1/5
    num_paper_sheets = 8
    envelope_weight = 2/5
    total_weight = (paper_weight * num_paper_sheets) + envelope_weight
    num_stamps = total_weight
    result = num_stamps
    return result

print(solution())