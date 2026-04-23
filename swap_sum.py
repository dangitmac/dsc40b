def swap_sum(A, B):
    sum_A = sum(A)
    sum_B = sum(B)

    difference = sum_A - sum_B + 10

    if difference % 2 != 0:
        return None

    target = difference // 2

    a_index = 0
    b_index = 0

    while a_index < len(A) and b_index < len(B):
        current = A[a_index] - B[b_index]

        if current == target:
            return (a_index, b_index)
        elif current < target:
            a_index += 1
        else:
            b_index += 1

    return None
