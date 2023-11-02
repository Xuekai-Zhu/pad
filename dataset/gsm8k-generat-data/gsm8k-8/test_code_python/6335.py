def solution():
    # Define the total number of vegetables
    total_vegetables = 280

    # Define the ratio of tomatoes to cucumbers as 3 to 1
    tomato_to_cucumber_ratio = 3/1

    # Calculate the number of tomatoes
    tomato_count = total_vegetables / (tomato_to_cucumber_ratio + 1) * tomato_to_cucumber_ratio

    # Calculate the number of cucumbers
    cucumber_count = total_vegetables - tomato_count

    result = cucumber_count
    return result

print(solution())