def solution():
    """Mcdonald is planning to open up a farm that provides eggs to the community. In his local community, Saly needs 10 eggs, Ben needs 14 eggs, and Ked needs half of the number of eggs needed by Ben per week. In a month which has 4 weeks, how many eggs should Mcdonald's farm produce?"""
    saly_eggs = 10
    ben_eggs = 14
    ked_eggs = ben_eggs / 2
    eggs_needed_per_week = saly_eggs + ben_eggs + ked_eggs
    eggs_needed_per_month = eggs_needed_per_week * 4
    result = eggs_needed_per_month
    
    return result

print(solution())