def solution():
    """Three people divided an amount of $1920. The second took $80 more than the first and the third took twice what the second took. Calculate the share of the first one."""
    total_amount = 1920
    second_person_share = first_person_share + 80
    third_person_share = 2 * second_person_share
    sum_of_shares = first_person_share + second_person_share + third_person_share
    first_person_share = (total_amount * first_person_share) / sum_of_shares
    result = first_person_share
    return result

print(solution())