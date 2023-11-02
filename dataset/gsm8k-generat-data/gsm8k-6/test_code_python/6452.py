def solution():
    # Calculate the total number of stickers Elizabeth uses
    remaining_bottles = 10 - 2 - 1  # Elizabeth loses 2 water bottles at school, and 1 is stolen at dance practice
    total_stickers = remaining_bottles * 3  # Elizabeth places 3 stickers on each remaining water bottle
    result = total_stickers
    return result

print(solution())