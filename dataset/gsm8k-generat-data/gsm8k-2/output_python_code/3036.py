def solution():
    """After a visit to the newly opened aquarium, 40 percent of the aquarium visitors fell ill from a mysterious disease. If there were 500 visitors, how many of them did not fall ill?"""
    total_visitors = 500
    ill_percentage = 0.4
    ill_visitors = total_visitors * ill_percentage
    healthy_visitors = total_visitors - ill_visitors
    result = healthy_visitors
    return result

print(solution())