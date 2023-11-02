def solution():
    # Define the available low calorie options for brunch and lunch at McDonald's
    brunch_options = ["parfaits", "egg white sandwiches"]
    lunch_options = ["basic hamburgers", "salads"]
    # Check if there are any low calorie lunch options available
    if lunch_options:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())