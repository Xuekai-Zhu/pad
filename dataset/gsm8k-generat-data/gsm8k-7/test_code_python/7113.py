def solution():
    buckets = [11, 13, 12, 16, 10]
    target_sum = 23
    
    # Find two buckets that add up to 23
    for i in range(len(buckets)):
        for j in range(i+1, len(buckets)):
            if buckets[i]+buckets[j] == target_sum:
                # Remove the two used buckets from the list
                buckets.pop(j)
                buckets.pop(i)
                break
        if len(buckets) == 3:
            break
    
    # Calculate the total amount of water in the second large bucket
    total_water = sum(buckets)
    result = total_water
    return result

print(solution())