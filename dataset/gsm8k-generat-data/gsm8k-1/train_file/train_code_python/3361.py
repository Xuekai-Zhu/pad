def solution():
    """The American swallow can lift into the air and carry a maximum of 5 pounds of weight, while the European swallow can lift and carry twice the weight as the American swallow. If there was a flock of 90 swallows, containing twice as many American as European swallows, what is the maximum combined weight the flock can carry?"""
    american_swallow_weight = 5
    european_swallow_weight = american_swallow_weight * 2
    num_american_swallows = 2/3 * 90
    num_european_swallows = 1/3 * 90
    total_weight = (num_american_swallows * american_swallow_weight) + (num_european_swallows * european_swallow_weight)
    result = total_weight
    return result

print(solution())