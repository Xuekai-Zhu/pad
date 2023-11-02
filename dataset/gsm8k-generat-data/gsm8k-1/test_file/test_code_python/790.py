def solution():
    """A zookeeper is counting how many lions are in their enclosure. She counts 12 female lions, half as many male lions, and 14 lion cubs. How many lions are in the enclosure?"""
    num_female_lions = 12
    num_male_lions = num_female_lions / 2
    num_lion_cubs = 14
    total_lions = num_female_lions + num_male_lions + num_lion_cubs
    
    return total_lions

print(solution())