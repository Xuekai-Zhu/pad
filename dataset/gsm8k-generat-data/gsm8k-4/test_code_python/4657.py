def solution():
    """Fatima has a piece of cloth that is 100 square inches big. She has decided to cut the cloth in half. She plans on keeping half and donating the other half. If she does this 2 times, then how much cloth will she have donated?"""
    # Define the initial size of the cloth
    cloth_size = 100

    # Cut the cloth in half and donate one half
    donated_cloth = cloth_size / 2

    # Cut the remaining cloth in half and donate another half
    donated_cloth += donated_cloth / 2

    # return the result
    result = donated_cloth
    return result

print(solution())