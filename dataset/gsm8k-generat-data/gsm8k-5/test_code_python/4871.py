def solution():
    total_chickens = 80  # Mrs. Fredrickson has 80 chickens
    roosters = total_chickens / 4  # 1/4 of the chickens are roosters
    hens = total_chickens - roosters  # The rest of the chickens are hens
    laying_hens = 3/4 * hens  # Only 3/4 of the hens lay eggs
    non_laying_hens = hens - laying_hens  # The remaining hens do not lay eggs

    # Calculate the total number of chickens that do not lay eggs
    total_non_laying_chickens = roosters + non_laying_hens
    result = total_non_laying_chickens
    return result

print(solution())