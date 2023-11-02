def solution():
    num_stickers_per_page = 20
    num_pages = 12
    pages_lost = 1

    # Calculate the total number of stickers before losing a page
    total_stickers_before_loss = num_stickers_per_page * num_pages

    # Calculate the total number of stickers after losing a page
    total_stickers_after_loss = num_stickers_per_page * (num_pages - pages_lost)

    # Calculate the number of stickers lost
    num_lost_stickers = total_stickers_before_loss - total_stickers_after_loss
    result = total_stickers_after_loss
    return result

print(solution())