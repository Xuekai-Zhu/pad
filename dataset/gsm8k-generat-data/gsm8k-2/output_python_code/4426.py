def solution():
    """At the park, Naomi saw people riding 7 regular bikes and 11 children’s bikes. Regular bikes have 2 wheels and kid’s bikes have 4 wheels. How many wheels did Naomi see at the park?"""
    regular_bikes = 7
    children_bikes = 11
    regular_wheels = 2 * regular_bikes
    children_wheels = 4 * children_bikes
    total_wheels = regular_wheels + children_wheels
    result = total_wheels
    return result

print(solution())