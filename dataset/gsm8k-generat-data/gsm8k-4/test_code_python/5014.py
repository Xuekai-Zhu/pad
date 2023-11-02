def solution():
    """Ellen is painting flowers on a vase. It takes her 5 minutes to paint a lily, 7 minutes to paint a rose, 3 minutes to paint an orchid, and 2 minutes to paint a vine. How long will it take her to paint 17 lilies, 10 roses, 6 orchids and 20 vines?"""
    # Define the time it takes to paint each flower
    lily_time = 5
    rose_time = 7
    orchid_time = 3
    vine_time = 2

    # Calculate the total time to paint all the flowers
    total_time = (lily_time * 17) + (rose_time * 10) + (orchid_time * 6) + (vine_time * 20)

    # Return the result in minutes
    result = total_time
    return result

print(solution())