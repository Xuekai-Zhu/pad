def solution():
    num_first_10_stories = 10
    height_first_10_stories = 12

    num_remaining_stories = 10
    additional_height_per_story = 3

    # Calculate the total height of the first 10 stories
    total_first_10_stories_height = num_first_10_stories * height_first_10_stories

    # Calculate the total height of the remaining stories
    total_remaining_stories_height = num_remaining_stories * (height_first_10_stories + additional_height_per_story)

    # Calculate the total height of the building
    total_height = total_first_10_stories_height + total_remaining_stories_height
    result = total_height
    return result

print(solution())