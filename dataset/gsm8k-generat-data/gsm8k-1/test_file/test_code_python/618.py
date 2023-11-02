def solution():
    """Jim has a 20 pack of gum. He chews 1 piece of gum for every 2 hours he's at school over a school day that lasts 8 hours. He chews 1 piece on the way home from school and 1 stick after dinner. He also gives half the gum he has remaining to his sister when she asks for some right before bed. How many pieces of gum does Jim have left at the end of the day?"""
    gum_pack = 20
    gum_at_school = 4
    gum_after_school = 1
    gum_after_dinner = 1
    gum_left = gum_pack - (gum_at_school + gum_after_school + gum_after_dinner)
    gum_left /= 2  # half given to sister
    result = gum_left
    return result

print(solution())