def solution():
    """Fatima has a piece of cloth that is 100 square inches big. She has decided to cut the cloth in half. She plans on keeping half and donating the other half. If she does this 2 times, then how much cloth will she have donated?"""
    initial_size = 100
    donated_size = 0 # initialize donated size to zero
    for i in range(2):
        donated_size += initial_size/2
        initial_size /= 2 # divide the remaining cloth size by half
    result = donated_size
    return result

print(solution())