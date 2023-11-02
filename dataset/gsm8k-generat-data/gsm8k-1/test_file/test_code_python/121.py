def solution():
    """Julia was preparing for a dinner party at her house, where she intended to serve stew. She noticed that she was out of plastic spoons, so she bought a new package of spoons. Later, her husband also bought a package of 5 new spoons and gave them to Julia. While Julia was making the stew, she used three of the spoons to sample her stew. Later, when she went to set the table, she had a total of 12 spoons. How many spoons were in the package that Julia bought?"""
    initial_package = 0
    husband_package = 5
    sample_spoons = 3
    final_spoons = 12
    initial_package = final_spoons - husband_package - sample_spoons
    result = initial_package
    return result

print(solution())