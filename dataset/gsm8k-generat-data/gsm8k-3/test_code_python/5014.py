def solution():
    """Ellen is painting flowers on a vase. It takes her 5 minutes to paint a lily, 7 minutes to paint a rose, 3 minutes to paint an orchid, and 2 minutes to paint a vine. How long will it take her to paint 17 lilies, 10 roses, 6 orchids and 20 vines?"""
    # Define the time it takes to paint each type of flower
    LILY_TIME = 5
    ROSE_TIME = 7
    ORCHID_TIME = 3
    VINE_TIME = 2

    # Define the number of each type of flower to be painted
    num_lilies = 17
    num_roses = 10
    num_orchids = 6
    num_vines = 20

    # Calculate the total time it will take to paint all the flowers
    total_time = (num_lilies * LILY_TIME) + (num_roses * ROSE_TIME) + (num_orchids * ORCHID_TIME) + (num_vines * VINE_TIME)

    # Display the total time
    result = total_time
    return result

print(solution())