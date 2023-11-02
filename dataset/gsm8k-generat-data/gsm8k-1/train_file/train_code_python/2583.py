def solution():
    """Belinda’s dog is missing, so she made 200 flyers to distribute around town with the help of her friends. Ryan passed out 42 flyers, Alyssa passed out 67, Scott passed out 51 and Belinda passed out the rest. What percentage of the flyers did Belinda pass out?"""
    total_flyers = 200
    flyers_passed_out = 42 + 67 + 51
    belinda_flyers = total_flyers - flyers_passed_out
    percentage = (belinda_flyers / total_flyers) * 100
    result = percentage
    return result

print(solution())