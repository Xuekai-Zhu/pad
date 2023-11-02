def solution():
    """It takes Nissa 10 seconds to clip each of her cats' nails. 90 seconds to clean each of her ears, and 5 minutes to shampoo her. If the cat has four claws on each foot, how many seconds does grooming her cat take total?"""
    nail_time = 4 * 10  # 4 claws per foot
    ear_time = 2 * 90  # assuming 2 ears to clean
    shampoo_time = 5 * 60
    total_time = nail_time + ear_time + shampoo_time
    result = total_time
    return result

print(solution())