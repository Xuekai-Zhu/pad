def solution():
    
    num_roses = 20
    num_lilies = int(num_roses * 0.75)
    rose_cost = 5
    lily_cost = 2 * rose_cost
    total_cost = (num_roses * rose_cost) + (num_lilies * lily_cost)
    result = total_cost
    return result

print(solution())