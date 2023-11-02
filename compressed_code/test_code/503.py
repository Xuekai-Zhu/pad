def solution():
    
    total_savings = 150
    savings_jan_to_jul = 10 * 7
    savings_aug_to_nov = 15 * 4
    total_savings_so_far = savings_jan_to_jul + savings_aug_to_nov
    remaining_savings_needed = total_savings - total_savings_so_far
    savings_in_december = remaining_savings_needed
    return savings_in_december

print(solution())