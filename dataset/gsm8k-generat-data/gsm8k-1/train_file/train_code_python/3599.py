def solution():
    """Pat's stick is 30 inches long. He covers 7 inches of the stick in dirt. The portion that is not covered in dirt is half as long as Sarah’s stick. Jane’s stick is two feet shorter than Sarah’s stick. How many inches long is Jane’s stick?"""
    pat_stick = 30
    pat_dirty = 7
    pat_clean = pat_stick - pat_dirty
    
    sarah_stick = pat_clean * 2
    
    jane_stick = (sarah_stick - 24) * 12 # convert 2 feet to 24 inches
    
    result = jane_stick
    return result

print(solution())