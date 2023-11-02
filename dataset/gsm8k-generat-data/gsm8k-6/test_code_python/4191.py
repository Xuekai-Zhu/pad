def solution():
    # Find how much experience James and John had 8 years ago
    James_8_years_ago = 20 - 8
    John_8_years_ago = James_8_years_ago * 2

    # Find how much experience John has now
    John_now = John_8_years_ago + 8

    # Find how much experience Mike has
    Mike = John_now - 16

    # Find the total combined experience
    combined_experience = James_8_years_ago + John_8_years_ago + John_now + Mike
    result = combined_experience
    return result

print(solution())