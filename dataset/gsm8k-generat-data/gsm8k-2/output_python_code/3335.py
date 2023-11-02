def solution():
    """At the park, Dimitri saw families riding bicycles and tricycles. Bicycles have two wheels and tricycles have three wheels. 6 adults were riding bicycles and 15 children were riding tricycles. How many wheels did Dimitri see at the park?"""
    bicycle_count = 6
    tricycle_count = 15
    bicycle_wheels = 2 * bicycle_count
    tricycle_wheels = 3 * tricycle_count
    total_wheels = bicycle_wheels + tricycle_wheels
    result = total_wheels
    return result

print(solution())