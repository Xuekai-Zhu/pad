def solution():
    """Ellen is painting flowers on a vase. It takes her 5 minutes to paint a lily, 7 minutes to paint a rose, 3 minutes to paint an orchid, and 2 minutes to paint a vine. How long will it take her to paint 17 lilies, 10 roses, 6 orchids and 20 vines?"""
    time_per_lily = 5
    time_per_rose = 7
    time_per_orchid = 3
    time_per_vine = 2
    num_lilies = 17
    num_roses = 10
    num_orchids = 6
    num_vines = 20
    total_time = (time_per_lily * num_lilies) + (time_per_rose * num_roses) + (time_per_orchid * num_orchids) + (time_per_vine * num_vines)
    result = total_time
    return result

print(solution())