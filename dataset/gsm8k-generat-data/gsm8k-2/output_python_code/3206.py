def solution():
    """On a Sunday morning, Josephine sold milk in the farm stall. The buyers brought their containers. She filled three containers with two liters each, two containers with 0.75 liters each, and five containers with 0.5 liters each. How many liters of milk did Josephine sell in total?"""
    liters_sold = 0
    liters_sold += 3 * 2   # 3 containers with 2 liters each
    liters_sold += 2 * 0.75  # 2 containers with 0.75 liters each
    liters_sold += 5 * 0.5  # 5 containers with 0.5 liters each
    result = liters_sold
    return result

print(solution())