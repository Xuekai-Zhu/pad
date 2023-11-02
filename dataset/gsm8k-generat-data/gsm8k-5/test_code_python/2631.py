def solution():
    shirts_per_day = 3  # Jenson makes 3 shirts per day
    pants_per_day = 5  # Kingsley makes 5 pairs of pants per day
    yards_per_shirt = 2  # Each shirt uses 2 yards of fabric
    yards_per_pant = 5  # Each pair of pants uses 5 yards of fabric
    days = 3  # They want to know how many yards of fabric they need every 3 days

    # Calculate the total yards of fabric needed for shirts and pants separately
    total_yards_shirts = shirts_per_day * yards_per_shirt * days
    total_yards_pants = pants_per_day * yards_per_pant * days

    # Calculate the total yards of fabric needed for both shirts and pants
    total_yards = total_yards_shirts + total_yards_pants
    result = total_yards
    return result

print(solution())