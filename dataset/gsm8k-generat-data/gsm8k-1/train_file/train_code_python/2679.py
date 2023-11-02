def solution():
    """James decides to try and collect rare artifacts in the field. He spends 6 months researching before going on a 2-year-long expedition for his first find. The second artifact takes 3 times as long for the research and discovery. How long did it take him to find both?"""
    research_time = 6
    artifact1_time = 2*12
    artifact2_time = artifact1_time * 3
    total_time = research_time + artifact1_time + artifact2_time
    result = total_time
    return result

print(solution())