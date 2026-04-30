import random

def knn_distance(arr, q, k):
    # make list of (distance, value)
    distance_pairs = [(abs(num - q), num) for num in arr]

    def quickselect(left, right, k_index):
        pivot_index = random.randint(left, right)
        distance_pairs[pivot_index], distance_pairs[right] = distance_pairs[right], distance_pairs[pivot_index]
        
        pivot_distance = distance_pairs[right][0]
        store_index = left

        for i in range(left, right):
            if distance_pairs[i][0] <= pivot_distance:
                distance_pairs[i], distance_pairs[store_index] = distance_pairs[store_index], distance_pairs[i]
                store_index += 1

        distance_pairs[store_index], distance_pairs[right] = distance_pairs[right], distance_pairs[store_index]

        if store_index == k_index:
            return distance_pairs[store_index]
        elif store_index < k_index:
            return quickselect(store_index + 1, right, k_index)
        else:
            return quickselect(left, store_index - 1, k_index)

    kth_distance, kth_value = quickselect(0, len(distance_pairs) - 1, k - 1)
    return kth_distance, kth_value
