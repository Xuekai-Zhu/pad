def solution():
    """The Doubtfire sisters are driving home with 7 kittens adopted from the local animal shelter when their mother calls to inform them that their two house cats have just had kittens. She says that Patchy, the first cat, has had thrice the number of adopted kittens, while Trixie, the other cat, has had 12. How many kittens does the Doubtfire family now have?"""
    adopted_kittens = 7
    trixie_kittens = 12
    patchy_kittens = 3 * adopted_kittens
    total_kittens = adopted_kittens + trixie_kittens + patchy_kittens
    result = total_kittens
    return result

print(solution())