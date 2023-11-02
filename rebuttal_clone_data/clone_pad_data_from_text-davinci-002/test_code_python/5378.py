def solution():
    first_10_stories = 10
    story_height = 12
    remaining_stories = 20 - first_10_stories
    additional_height = remaining_stories * 3
    total_height = first_10_stories * story_height + additional_height
    result = total_height
    return result

print(solution())