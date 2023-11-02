def solution():
    red_sea_max_depth = 3040
    nuno_gomes_max_depth = 318
    if nuno_gomes_max_depth < red_sea_max_depth:
        result = "no, it would not be very difficult for Nuno Gomes to dive to the Red Sea's deepest point"
    else:
        result = "yes, it would be very difficult for Nuno Gomes to dive to the Red Sea's deepest point"
    return result

print(solution())