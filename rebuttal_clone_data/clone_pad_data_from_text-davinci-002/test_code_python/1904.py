def solution():
     leaves_needed = 30
     bugs_needed = 20
     total_items_needed = leaves_needed + bugs_needed
     days_given = 10
     items_needed_per_day = total_items_needed / days_given
     result = items_needed_per_day

     return result

print(solution())