def mode(numbers):
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty")

    times_seen = {}
    most_common_number = numbers[0]
    highest_count = 0

    for current_number in numbers:
        if current_number not in times_seen:
            times_seen[current_number] = 1
        else:
            times_seen[current_number] += 1

        if times_seen[current_number] > highest_count:
            highest_count = times_seen[current_number]
            most_common_number = current_number

    return most_common_number
