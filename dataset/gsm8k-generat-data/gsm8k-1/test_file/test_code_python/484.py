def solution():
    """Jana has 27 puppies. Two thirds of Jana's puppies are Pomeranians. One third of the Pomeranians are girls. How many girl Pomeranians does Jana have?"""
    total_puppies = 27
    pomeranian_percentage = 2/3 
    pomeranian_count = total_puppies * pomeranian_percentage
    girl_percentage = 1/3
    girl_pomeranians = pomeranian_count * girl_percentage
    result = girl_pomeranians
    return result

print(solution())