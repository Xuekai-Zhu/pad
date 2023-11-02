def solution():
     """Alyssa, Keely, and Kendall ordered 100 chicken nuggets from a fast-food restaurant. Keely and Kendall each ate twice as many as Alyssa. How many did Alyssa eat?"""
     total_nuggets = 100
     keely_and_kendall_nuggets = 2 * total_nuggets / 3
     alyssa_nuggets = total_nuggets - keely_and_kendall_nuggets
     result = alyssa_nuggets
     return result

print(solution())