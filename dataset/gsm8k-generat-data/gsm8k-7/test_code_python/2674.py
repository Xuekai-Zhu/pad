def solution():
    monday_toys = 5
    tuesday_toys = 3 + 3 # 3 left from previous day and 3 new ones bought
    wednesday_toys = 5
    
    # Calculate the total number of dog toys Daisy has
    total_toys = monday_toys + tuesday_toys + wednesday_toys
    result = total_toys
    return result

print(solution())