def solution():
    peppers_for_very_spicy_curries = 3
    peppers_for_spicy_curries = 2
    peppers_for_mild_curries = 1
    very_spicy_curries_ordered = 30
    spicy_curries_ordered = 30
    mild_curries_ordered = 10
    peppers_used_for_very_spicy_curries = very_spicy_curries_ordered * peppers_for_very_spicy_curries
    peppers_used_for_spicy_curries = spicy_curries_ordered * peppers_for_spicy_curries
    peppers_used_for_mild_curries = mild_curries_ordered * peppers_for_mild_curries
    peppers_used_total = peppers_used_for_very_spicy_curries + peppers_used_for_spicy_curries + peppers_used_for_mild_curries
    very_spicy_curries_ordered = 0
    spicy_curries_ordered = 15
    mild_curries_ordered = 90

print(solution())