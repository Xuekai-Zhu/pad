def solution():
    # Calculate the number of packs of candy Antonov has left
    candies_left = 60 - 20  # Antonov gave a pack of candy to his sister
    packs_left = candies_left // 20  # calculate the number of packs left
    result = packs_left
    return result

print(solution())