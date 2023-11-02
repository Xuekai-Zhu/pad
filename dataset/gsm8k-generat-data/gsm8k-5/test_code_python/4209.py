def solution():
    dozen_cookies_per_recipe = 16  # The recipe makes 16 dozen cookies
    butter_per_recipe = 4  # The recipe calls for 4 pounds of butter
    desired_dozen_cookies = 4  # Valerie only wants to make 4 dozen cookies

    # Calculate the amount of butter needed for the desired number of cookies
    butter_needed = (desired_dozen_cookies / dozen_cookies_per_recipe) * butter_per_recipe
    result = butter_needed
    return result

print(solution())