def solution():
    
    # Define the number of bulk packs ordered and the number of bandages used on the first day
    PACKS_FIRST_DAY = 50
    BATCH_SIZE_FIRST_DAY = 38

    # Define the number of bandages used on the second day
    PACKS_SECOND_DAY = PACKS_FIRST_DAY - 10

    # Define the number of bandages used on the third day
    PACKS_THIRD_DAY = 2
    BATCH_SIZE_THIRD_DAY = 0.5

    # Calculate the total number of bandages used
    total_bandages_used = PACKS_FIRST_DAY + PACKS_SECOND_DAY + PACKS_THIRD_DAY

    # Calculate the number of bandages left at the end of the third day
    bandages_left = 78

    # Calculate the number of bandages used on the first day
    bandages_used = BATCH_SIZE_FIRST_DAY

    # Calculate the number of bandages left on the first day
    bandages_left_first_day = bandages_used -

print(solution())