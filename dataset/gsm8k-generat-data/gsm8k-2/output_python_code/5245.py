def solution():
    """Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?"""
    dog_count = [1, 2, 3]
    dog_time = [10, 7, 9]
    total_dogs = sum(dog_count)
    dog_fee = 20
    total_fee = 0
    for i in range(len(dog_count)):
        dog_fee_per_minute = 1 * dog_count[i]
        total_time = dog_time[i]
        total_fee += dog_fee + (dog_fee_per_minute * total_time)

    result = total_fee
    return result

print(solution())