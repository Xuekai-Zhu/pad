def solution():
    # Calculate how many months it has been since Bob last cut his hair
    months_since_cut = (36 - 6) / 0.5  # hair growth rate is 0.5 inches per month

    # Convert months to years
    years_since_cut = months_since_cut / 12

    result = years_since_cut
    return result

print(solution())