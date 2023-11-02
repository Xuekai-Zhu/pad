def solution():
    """Cynthia has three children whose ages add up to 35. Matthew is two years older than Rebecca and four years younger than Freddy. How many years old is Freddy?"""
    # Let's define the children's ages
    cynthia_children_age_sum = 35

    # Let's define the age relationship between Matthew, Rebecca, and Freddy
    matthew_age_diff_rebecca = 2
    matthew_age_diff_freddy = -4

    # Let's use math to solve for the age of each child
    # Let x be Rebecca's age
    # Then Matthew's age is x + 2
    # And Freddy's age is x + 2 - 4 = x - 2
    # The sum of their ages is x + (x+2) + (x-2) = 3x
    # So we can solve for x: 3x = 35 - 2 = 33 => x = 11
    rebecca_age = 11
    matthew_age = rebecca_age + matthew_age_diff_rebecca
    freddy_age = matthew_age + matthew_age_diff_freddy

    # The answer is Freddy's age
    result = freddy_age
    return result

print(solution())