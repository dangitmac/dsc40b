def histogram(points, bins):
    total_points = len(points)
    densities = []
    point_index = 0

    for start, end in bins:
        count_in_bin = 0

        while point_index < total_points and points[point_index] < end:
            count_in_bin += 1
            point_index += 1

        bin_width = end - start
        densities.append(count_in_bin / (total_points * bin_width))

    return densities
