def solution():
    
    original_stickers = 72
    stickers_given = 3 * 4
    given_to_mandy = stickers_given + 2
    given_to_justin = given_to_mandy - 10
    total_given = stickers_given + given_to_mandy + given_to_justin
    result = original_stickers - total_given
    return result

print(solution())