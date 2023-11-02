def solution():
    """Elizabeth has 10 reusable water bottles. She loses 2 water bottles at school. Then someone steals 1 of her water bottles at dance practice. To avoid any future theft of her water bottles, Elizabeth places 3 stickers on each of her remaining bottles. How many stickers does Elizabeth use in total on her water bottles?"""
    # Define the initial number of water bottles
    initial_bottles = 10

    # Calculate the number of lost or stolen water bottles
    lost_bottles = 2
    stolen_bottles = 1

    # Calculate the number of remaining water bottles
    remaining_bottles = initial_bottles - lost_bottles - stolen_bottles

    # Calculate the total number of stickers used
    stickers = remaining_bottles * 3

    # Return the result
    result = stickers
    return result

print(solution())