def solution():
    """Fatima has a piece of cloth that is 100 square inches big. She has decided to cut the cloth in half. She plans on keeping half and donating the other half. If she does this 2 times, then how much cloth will she have donated?"""
    initial_cloth = 100
    donated_cloth = 0
    for i in range(2):
        donated_cloth += initial_cloth / 2
        initial_cloth = initial_cloth / 2
    result = donated_cloth
    return result

print(solution())