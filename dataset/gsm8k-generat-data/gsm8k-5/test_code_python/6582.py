def solution():
    new_edition = 450  # The new edition has 450 pages
    old_edition = (new_edition + 230) / 2  # The new edition has 230 pages less than twice the old edition

    # Round the result up to the nearest whole number of pages
    old_edition = math.ceil(old_edition)

    result = old_edition
    return result

print(solution())