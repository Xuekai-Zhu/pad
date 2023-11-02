def solution():
    total_data = 500  # Elsa gets 500 MB of cell phone data each month
    youtube_data = 300  # Elsa spends 300 MB watching Youtube

    # Calculate how much data Elsa spends on Facebook
    remaining_data = total_data - youtube_data
    facebook_data = (2/5) * remaining_data

    # Calculate how much data Elsa has left
    remaining_data -= facebook_data
    result = remaining_data
    return result

print(solution())