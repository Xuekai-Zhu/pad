def solution():
    # Calculate the number of slices in the original loaf of bread
    # Emma started with x slices, Andy ate 3 slices, leaving (x-3) slices
    # She ends up with 1 slice and makes 10 pieces of toast, using 2 slices for each
    # So the remaining (x-3-1) slices must be enough for 10 pieces of toast
    # 2 slices of bread are needed for 1 piece of toast, so 10 pieces require 20 slices
    slices_original = 20 + 3 + 1  # total slices = slices used for toast + slices eaten by Andy + 1 slice left
    result = slices_original
    return result

print(solution())