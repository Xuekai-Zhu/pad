def solution():
    """Anna can read 1 page in 1 minute. Carole can read as fast as Anna but at half the speed of Brianna. How long does it take Brianna to read a 100-page book?"""
    anna_time = 100
    carole_time = anna_time * 2
    brianna_time = carole_time / 2
    total_time = brianna_time * 100
    result = total_time
    return result

print(solution())