def solution():
    """At the park, Dimitri saw families riding bicycles and tricycles. Bicycles have two wheels and tricycles have three wheels. 6 adults were riding bicycles and 15 children were riding tricycles. How many wheels did Dimitri see at the park?"""
    adults_on_bikes = 6
    children_on_trikes = 15
    wheels_on_bikes = 2
    wheels_on_trikes = 3
    total_wheels = (adults_on_bikes * wheels_on_bikes) + (children_on_trikes * wheels_on_trikes)
    result = total_wheels
    return result

print(solution())