def solution():
    """Darius has 5 buckets of water. One contains 11 ounces, one contains 13 ounces, one contains 12 ounces, one contains 16 ounces, and one contains 10 ounces. 
    He pours the ten-ounce bucket into a bigger bucket, along with one of the other four. The total in the bigger bucket is now 23 ounces. 
    He pours the remaining three buckets into a second large bucket. How many ounces does the second large bucket contain?"""
    # Define the initial buckets
    buckets = [11, 13, 12, 16, 10]

    # Find the two buckets that add up to 23
    for i in range(len(buckets)):
        for j in range(i+1, len(buckets)):
            if buckets[i] + buckets[j] == 23:
                # Remove the two buckets from the list
                buckets.pop(j)
                buckets.pop(i)
                break
        if len(buckets) == 3:
            break

    # Calculate the total number of ounces in the second large bucket
    total = sum(buckets)

    result = total
    return result

print(solution())