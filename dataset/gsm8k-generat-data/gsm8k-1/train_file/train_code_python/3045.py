def solution():
    """Kekai is running a sundae booth at the carnival. On Monday, he makes a total of 40 sundaes, and he puts 6 m&ms on each sundae. On Tuesday, he makes a total of 20 sundaes, and he puts 10 m&ms on each sundae. If each m&m pack contains 40 m&ms, how many m&m packs does Kekai use?"""
    mms_per_sundae_monday = 6
    mms_per_sundae_tuesday = 10 
    total_sundaes = 40 + 20
    total_mms = (40 * mms_per_sundae_monday) + (20 * mms_per_sundae_tuesday)
    packs_needed = total_mms / 40
    result = packs_needed
    return result

print(solution())