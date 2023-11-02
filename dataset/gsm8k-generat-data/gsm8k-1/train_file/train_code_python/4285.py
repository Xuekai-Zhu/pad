def solution():
    """Lizzy's school choir has a mixture of 80 blonde and black-haired girls. Their teacher decides to add 10 more girls to the choir, who turns out to be blonde. If there were 30 blonde-haired girls in the choir initially, how many black-haired girls are present?"""
    initial_blondes = 30
    initial_total = 80
    added_blondes = 10
    final_total = initial_total + added_blondes
    final_blondes = initial_blondes + added_blondes
    final_black_haired = final_total - final_blondes
    result = final_black_haired
    return result

print(solution())