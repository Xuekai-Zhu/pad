def solution():
    # Let's represent the number of ducks sold as x
    # Then the total earnings from selling x ducks and 5 chickens will be:

    earnings = (10 * x) + (8 * 5)

    # The farmer spends half of his earnings on a new wheelbarrow, so his remaining earnings are:
    remaining_earnings = earnings / 2

    # The buyer pays the farmer double what he paid for the wheelbarrow, so the farmer earned:
    additional_earnings = remaining_earnings + 60

    # we can set up an equation to solve for x:
    # 2*(earnings - x*10) = additional_earnings

    x = (earnings + additional_earnings) / 20

    result = x
    return result

print(solution())