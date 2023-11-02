def solution():
    hamburgers_sold = (4 * 2) + (2 * 2)  # Frank sold 4 hamburgers to 2 customers and 2 hamburgers to another 2 customers
    hamburgers_needed = (50 / 5) - hamburgers_sold  # Frank wants to make $50, and each hamburger sells for $5

    result = hamburgers_needed
    return result

print(solution())