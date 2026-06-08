def learn_theta(data, colors):

    biggest_blue_point = None
    smallest_red_point = None

    for index in range(len(data)):
        current_point = data[index]
        current_color = colors[index]

        if current_color == 'blue':
            if biggest_blue_point is None:
                biggest_blue_point = current_point
            elif current_point > biggest_blue_point:
                biggest_blue_point = current_point

        if current_color == 'red':
            if smallest_red_point is None:
                smallest_red_point = current_point
            elif current_point < smallest_red_point:
                smallest_red_point = current_point

    theta = (biggest_blue_point + smallest_red_point) / 2
    return theta


def compute_ell(data, colors, theta):

    loss = 0

    for index in range(len(data)):
        current_point = data[index]
        current_color = colors[index]

        red_on_wrong_side = current_color == 'red' and current_point <= theta
        blue_on_wrong_side = current_color == 'blue' and current_point > theta

        if red_on_wrong_side:
            loss += 1

        if blue_on_wrong_side:
            loss += 1

    return float(loss)


def minimize_ell(data, colors):

    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for possible_theta in data:
        current_loss = compute_ell(data, colors, possible_theta)

        if current_loss < best_loss:
            best_loss = current_loss
            best_theta = possible_theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):

    red_less_than_or_equal_theta = 0
    blue_greater_than_theta = 0

    for color in colors:
        if color == 'blue':
            blue_greater_than_theta += 1

    best_theta = data[0]
    best_loss = red_less_than_or_equal_theta + blue_greater_than_theta

    for index in range(len(data)):
        current_theta = data[index]
        current_color = colors[index]

        if current_color == 'red':
            red_less_than_or_equal_theta += 1

        if current_color == 'blue':
            blue_greater_than_theta -= 1

        current_loss = (
            red_less_than_or_equal_theta
            + blue_greater_than_theta
        )

        if current_loss < best_loss:
            best_loss = current_loss
            best_theta = current_theta

    return float(best_theta)
