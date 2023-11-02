def solution():
    """Olivia gave William 10 napkins. Amelia also gives William twice the number of napkins Olivia gave him. If William had 15 napkins before, how many napkins does he have now?"""
    olivia_napkins = 10
    amelia_napkins = olivia_napkins * 2
    total_napkins = olivia_napkins + amelia_napkins + 15
    result = total_napkins
    return result

print(solution())