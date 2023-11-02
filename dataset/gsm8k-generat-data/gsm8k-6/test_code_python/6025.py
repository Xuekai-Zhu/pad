def solution():
    # Count the total number of pens Kendra and Tony have
    kendra_pens = 4 * 3  # 4 packs of pens with 3 pens each
    tony_pens = 2 * 3  # 2 packs of pens with 3 pens each
    total_pens = kendra_pens + tony_pens

    # Calculate the number of friends they can give pens to
    remaining_pens = total_pens - 4  # keep 2 pens each
    friends = remaining_pens // 1  # distribute the remaining pens to friends, one pen per friend

    result = friends
    return result

print(solution())