def solution():
    """Harper collected 30% more pieces of Halloween candy than her sister Maggie, who only collected 50 pieces.  Neil collected 40% more candy than Harper.  How much candy did Neil get on Halloween?"""
    # Define Maggie's candy count
    maggie_candy = 50

    # Calculate Harper's candy count
    harper_candy = maggie_candy * 1.3

    # Calculate Neil's candy count
    neil_candy = harper_candy * 1.4

    result = neil_candy
    return result

print(solution())