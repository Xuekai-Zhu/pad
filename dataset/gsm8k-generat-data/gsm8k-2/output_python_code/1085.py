def solution():
    """Mr. Alonzo harvested 245.5 kg of tomatoes. He sold 125.5 kg to Mrs. Maxwell and 78 kg to Mr. Wilson. How many kilograms of tomatoes are not sold?"""
    harvested = 245.5
    sold_to_maxwell = 125.5
    sold_to_wilson = 78
    total_sold = sold_to_maxwell + sold_to_wilson
    not_sold = harvested - total_sold
    result = not_sold
    return result

print(solution())