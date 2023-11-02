def solution():
    """Samantha has 12 fewer paintings than Shelley, and Shelley has 8 paintings more than Kim. If Samantha has 27 paintings, how many paintings does Kim have?"""
    samantha_paintings = 27
    shelley_paintings = samantha_paintings + 12
    kim_paintings = shelley_paintings - 8
    result = kim_paintings
    return result

print(solution())