def solution():
    
    total_animals = 84
    squirrels = 6
    raccoons = 1
    total_squirrels = squirrels * raccoons
    total_raccoons = (total_animals / (total_squirrels + raccoons)) * raccoons
    result = total_raccoons
    return result

print(solution())