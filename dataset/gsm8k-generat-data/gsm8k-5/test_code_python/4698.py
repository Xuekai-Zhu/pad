def solution():
    num_family_members = 5  # Andrew lives with his 2 parents and 2 siblings
    masks_per_person = 1  # Each person uses 1 mask every 4 days
    total_masks_used_per_day = num_family_members * masks_per_person / 4  # Calculate how many masks are used daily
    num_masks_in_pack = 100  # Andrew's father bought a package of 100 masks

    # Calculate how many days it will take to finish the pack of masks
    num_days = num_masks_in_pack / total_masks_used_per_day
    result = num_days
    return result

print(solution())