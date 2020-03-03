def switch_average(letter):
    switcher = {
        'A': '90 - 100',
        'B': '80 - 89',
        'C': '70 - 79',
        'D': '60 - 69',
        'F': '0 - 59'
    }
    return switcher.get(letter, "Invalid Input")


if __name__ == '__main__':
    switch_average()