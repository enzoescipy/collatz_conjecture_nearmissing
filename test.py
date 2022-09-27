
def gradial_even(num):
    div_left = num % 2
    if div_left > 1.0:
        div_left -= 1.0
    return div_left
print(gradial_even(4.0 % 2))