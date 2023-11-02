def solution():
    """Jason is tired of the neighborhood animals raiding his trash. He pepper-sprays some raccoons and 6 times as many squirrels. If he pepper-sprays 84 animals total, how many raccoons does he pepper-spray?"""
    total_animals = 84
    squirrels = 6
    raccoons = 1
    total_squirrels = squirrels * raccoons
    total_raccoons = (total_animals / (total_squirrels + raccoons)) * raccoons
    result = total_raccoons
    return result

print(solution())