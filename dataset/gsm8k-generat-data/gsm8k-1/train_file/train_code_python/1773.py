def solution():
    """Sedrach has 13 apple pies. If every apple pie can be quickly divided into halves and every half an apple pie can be split into 5 bite-size samples, how many people can taste Sedrach's apple pie if he divides them all into bite-size samples?"""
    apple_pies = 13
    half_pie = 2
    samples = 5
    total_samples = apple_pies * half_pie * samples
    result = total_samples
    return result

print(solution())