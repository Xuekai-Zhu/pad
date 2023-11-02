def solution():
    """Claire earns 1 girl scout badge every month. It takes Amber twice as long to earn a badge than Claire. Wendy earns three times the amount of badges as Claire in the same time frame. How many more badges does Wendy earn compared to Amber in a 1 year time frame?"""
    claire_badges = 1
    amber_badges = claire_badges / 2
    wendy_badges = claire_badges * 3
    badges_per_year = 12
    wendy_yearly_badges = wendy_badges * badges_per_year
    amber_yearly_badges = amber_badges * badges_per_year
    badges_difference = wendy_yearly_badges - amber_yearly_badges
    result = badges_difference
    return result

print(solution())