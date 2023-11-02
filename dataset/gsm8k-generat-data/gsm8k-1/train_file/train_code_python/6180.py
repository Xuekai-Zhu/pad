def solution():
    """Antonia is trying to improve her health by buying supplements. She has a 7-day pill box she wants to fill. She buys 5 different supplements. 3 of the bottles have 120 pills in them each. 2 of the bottles have 30 pills each. After Antonia has filled her pillbox with one pill of each supplement for 2 weeks, how many pills total does she have left from all 5 bottles?"""
    pills_per_box = 35
    total_pills = ((3*120) + (2*30)) - (5*2*pills_per_box)
    result = total_pills
    return result

print(solution())