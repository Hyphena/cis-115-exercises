from tkinter import W


row_length = float(input('Please enter the length of the row (ft): '))
end_post_length = float(input('Please enter the amount of space used '
    'by an end-post assembly (ft): '))
spacing_length = float(input('Please enter the space between the vines '
    '(ft): '))
grapevines = int((row_length - 2 * end_post_length) / spacing_length)

print(f'   You will be able to fit {grapevines:,d} grapevines.')
