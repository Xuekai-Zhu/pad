def solution():
    # Calculate how many boys were present
    total_present = 250 - 140
    boys_present = total_present / 3
    
    # Calculate how many boys were absent
    boys_absent = total_present - boys_present
    
    result = boys_absent
    return result

print(solution())