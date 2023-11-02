def solution():
    """Heather bought a jumbo bag of raisins with 27 cups of raisins in it. She wants to make oatmeal cookies, granola, and snack mix with the raisins. A batch of oatmeal cookies takes 3/4 of a cup of raisins. How many batches of oatmeal cookies can Heather make if she divides the bag of raisins equally among the cookies, granola, and snack mix?"""
    raisins_per_bag = 27
    raisins_per_cookie = 3/4
    total_cookies = raisins_per_bag // raisins_per_cookie / 3
    result = total_cookies
    return result

print(solution())