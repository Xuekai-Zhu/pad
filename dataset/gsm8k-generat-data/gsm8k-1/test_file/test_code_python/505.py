def solution():
    """Sophia and Rose went together to the market to buy onions and potatoes. Rose bought 4 times the number of onions and potatoes Sophia bought. If Rose bought 12 onions and 4 potatoes, how many onions and potatoes in total did Sophia buy at the market?"""
    rose_onions = 12
    rose_potatoes = 4
    rose_total = rose_onions + rose_potatoes
    rose_ratio = 4
    sophia_ratio = 1
    sophia_total = rose_total / (rose_ratio + sophia_ratio) * sophia_ratio
    sophia_onions = sophia_total / 2
    sophia_potatoes = sophia_total / 2
    result = sophia_total
    
    return result

print(solution())