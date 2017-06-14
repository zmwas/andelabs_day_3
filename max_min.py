def find_max_min(numbers=[]):
    output = []

    numbers.sort()

    largest= numbers[len(numbers)-1]
    smallest = numbers[0]

    output.append(smallest)
    output.append(largest)
    if smallest == largest:
        output.pop(0)

    return output

