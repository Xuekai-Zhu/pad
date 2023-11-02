def solution():
    
    contracted_units = 2000
    first_half_units = contracted_units * 3/5
    remaining_units = contracted_units - first_half_units - 300
    result = remaining_units
    return result

print(solution())