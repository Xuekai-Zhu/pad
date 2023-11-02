def solution():
    """Bill thought he bought 70 chihuahuas, but some of them turned out to be rats. If the number of rats was 6 times the number of chihuahuas, how many rats did he buy?"""
    total_animals = 70
    ratio_of_rats_to_chihuahuas = 6
    total_rats = (total_animals / (1 + ratio_of_rats_to_chihuahuas)) * ratio_of_rats_to_chihuahuas
    result = total_rats
    return result

print(solution())