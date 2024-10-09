num_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
iterator = iter(num_list)

while True:
    value = next(iterator)
    if value == 0:
        continue
    elif value < 0:
        break
    print(value)
