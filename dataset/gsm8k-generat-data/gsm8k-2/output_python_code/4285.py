def solution():
    """Lizzy's school choir has a mixture of 80 blonde and black-haired girls. Their teacher decides to add 10 more girls to the choir, who turns out to be blonde. If there were 30 blonde-haired girls in the choir initially, how many black-haired girls are present?"""
    initial_blondes = 30
    initial_total = 80
    new_blondes = 10
    total_with_new = initial_total + new_blondes
    new_black_haired = total_with_new - (initial_blondes + new_blondes)
    result = new_black_haired
    return result

print(solution())