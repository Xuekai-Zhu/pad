def solution():
    # Calculate the number of men and women in the office
    total_workers = 90
    men = total_workers * (2/3)
    women = total_workers - men

    # Calculate the new number of women in the office after hiring 10 more
    new_women = women + 10

    # Calculate the new percentage of women in the office
    total_workers += 10
    new_percentage = (new_women / total_workers) * 100
    result = new_percentage
    return result

print(solution())