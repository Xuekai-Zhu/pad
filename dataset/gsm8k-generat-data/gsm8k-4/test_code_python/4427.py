def solution():
    """At the park, Naomi saw people riding 7 regular bikes and 11 children’s bikes. Regular bikes have 2 wheels and kid’s bikes have 4 wheels. How many wheels did Naomi see at the park?"""
    # Define the number of regular bikes and children's bikes
    regular_bikes = 7
    children_bikes = 11

    # Define the number of wheels on regular bikes and children's bikes
    regular_wheels = 2
    children_wheels = 4

    # Calculate the total number of wheels
    total_wheels = (regular_bikes * regular_wheels) + (children_bikes * children_wheels)

    result = total_wheels
    return result

print(solution())