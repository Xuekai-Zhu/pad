def solution():
    """Alexis can sew a skirt in 2 hours and a coat in 7 hours. How long does it take for Alexis to sew 6 skirts and 4 coats?"""
    skirt_time = 2
    coat_time = 7
    num_skirts = 6
    num_coats = 4
    total_time = (skirt_time * num_skirts) + (coat_time * num_coats)
    result = total_time
    return result

print(solution())