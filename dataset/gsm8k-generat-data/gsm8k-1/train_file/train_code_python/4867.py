def solution():
    """Ishmael was monitoring whales out at sea for conservation purposes. Each time he takes a trip to sea, he sees a different group of whales. On his first trip, he counts 28 male whales and twice as many female whales. On his second trip, he sees 8 baby whales, each travelling with their parents. On his third trip, he counts half as many male whales as the first trip and the same number of female whales as on the first trip. In total, how many whales were out at sea during Ishmael’s monitoring?"""
    male_whales_1 = 28
    female_whales_1 = male_whales_1 * 2
    baby_whales_2 = 8
    male_whales_3 = male_whales_1 / 2
    female_whales_3 = female_whales_1
    total_whales = male_whales_1 + female_whales_1 + baby_whales_2 + male_whales_3 + female_whales_3
    result = total_whales
    return result

print(solution())