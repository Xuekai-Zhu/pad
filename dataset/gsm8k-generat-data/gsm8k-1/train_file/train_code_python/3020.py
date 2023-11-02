def solution():
    """Jessica wrote a long letter to her aunt and needed to put stamps on it to mail it. She used eight pieces of paper that weigh 1/5 of an ounce each, and her envelope weighs 2/5 of an ounce. She needed one stamp per ounce. How many stamps did Jessica need to mail her letter?"""
    paper_weight = 1/5
    total_paper_weight = 8 * paper_weight
    envelope_weight = 2/5
    total_weight = total_paper_weight + envelope_weight
    stamps_needed = total_weight
    result = stamps_needed
    return result

print(solution())