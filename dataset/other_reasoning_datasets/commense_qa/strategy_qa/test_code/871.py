def solution():
    # Define that cucumbers are a vegetable, carrot cake is an exception, and cucumbers are not in carrot cake
    cucumber_is_vegetable = True
    desserts_not_made_with_vegetables = True
    cucumber_not_in_carrot_cake = True
    # Check if cucumbers are often found in dessert
    if cucumber_is_vegetable and desserts_not_made_with_vegetables and cucumber_not_in_carrot_cake:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())