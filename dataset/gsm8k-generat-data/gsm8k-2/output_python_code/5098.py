def solution():
    """Yesterday, the newly opened animal shelter received their first 60 animals. They got 20 more cats than dogs. How many cats did they take in?"""
    total_animals = 60
    cat_dog_diff = 20
    cat_count = (total_animals + cat_dog_diff) / 2
    result = cat_count
    return result

print(solution())