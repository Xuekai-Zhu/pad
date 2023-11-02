def solution():
    """Elizabeth has 10 reusable water bottles. She loses 2 water bottles at school. Then someone steals 1 of her water bottles at dance practice. To avoid any future theft of her water bottles, Elizabeth places 3 stickers on each of her remaining bottles. How many stickers does Elizabeth use in total on her water bottles?"""
    # Define the initial number of water bottles
    num_bottles = 10

    # Lose 2 water bottles at school
    num_bottles -= 2

    # Someone steals 1 water bottle at dance practice
    num_bottles -= 1

    # Add 3 stickers to each remaining water bottle
    num_stickers = num_bottles * 3

    # Display the total number of stickers used
    result = num_stickers
    return result

print(solution())