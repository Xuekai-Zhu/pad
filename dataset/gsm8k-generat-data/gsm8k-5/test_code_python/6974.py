def solution():
    members = 4  # There are four members in the household
    bread_per_day = (3 * 2 + 2 * 2) * members  # Each member consumes 3 slices for breakfast and 2 slices for snacks
    slices_per_loaf = 12  # A loaf of bread has 12 slices
    loaves_per_day = bread_per_day / slices_per_loaf  # Calculate the number of loaves consumed per day
    loaves_5_days = loaves_per_day * 5  # Calculate the number of loaves consumed in 5 days
    result = loaves_5_days
    return result

print(solution())