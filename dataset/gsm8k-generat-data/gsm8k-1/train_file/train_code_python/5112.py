def solution():
    """Two birds making a nest each made 10 round trips collecting building materials. If the building materials were located 200 miles from where they were building the nest, what is the total distance the birds covered in the trips?"""
    num_birds = 2
    round_trips = 10
    distance_per_round_trip = 400 # 200 miles there and 200 miles back
    total_distance = num_birds * round_trips * distance_per_round_trip
    result = total_distance
    return result

print(solution())