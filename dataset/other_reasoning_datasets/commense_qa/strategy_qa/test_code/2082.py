def solution():
    horseradish_height = 4.9
    newborn_height = 0.43 # Convert 20 inches to feet
    if newborn_height < horseradish_height:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())