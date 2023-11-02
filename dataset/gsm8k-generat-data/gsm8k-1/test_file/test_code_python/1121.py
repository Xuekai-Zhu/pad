def solution():
    """John packs M&M in small bags to eat. He buys 3 large bags weighing 10 ounces each. If an ounce of M&M has 30 M&M in it how many small bags can he make if he puts 10 in each small bag?"""
    bags_per_ounce = 30
    ounces_per_bag = 10
    m_and_ms_total = bags_per_ounce * ounces_per_bag * 3
    m_and_ms_per_small_bag = 10
    bags_possible = m_and_ms_total / m_and_ms_per_small_bag
    result = bags_possible
    return result

print(solution())