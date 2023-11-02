def solution():
    """1 chocolate bar costs $1.50 and can be broken into 3 sections to make 3 s'mores. Ron is hosting a boy scout camp out in his backyard for 15 scouts. He wants to make sure that there are enough chocolate bars for everyone to have 2 s'mores each. How much will he spend on chocolate bars?"""
    chocolate_bar_cost = 1.5
    sections_per_bar = 3
    s'mores_per_section = 1
    s'mores_per_person = 2
    scouts = 15
    total_s'mores = scouts * s'mores_per_person
    total_sections_needed = total_s'mores / s'mores_per_section
    total_bars_needed = total_sections_needed / sections_per_bar
    total_cost = total_bars_needed * chocolate_bar_cost
    result = total_cost
    return result

print(solution())