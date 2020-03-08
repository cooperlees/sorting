#!/usr/bin/env python3

import argparse
import sys
from copy import copy
from random import random
from time import time
from typing import Dict, List


def bubble_sort(nums: List[float]) -> None:
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


def _heapify(nums: List[float], heap_size: int, root_index: int) -> None:
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        _heapify(nums, heap_size, largest)


def heap_sort(nums: List[float]) -> None:
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        _heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        _heapify(nums, i, 0)


def insertion_sort(nums: List[float]) -> None:
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


def _merge(left_list: List[float], right_list: List[float]) -> List[float]:
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums: List[float]):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return _merge(left_list, right_list)


def selection_sort(nums: List[float]) -> None:
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def _partition(nums: List[float], low: int, high: int) -> int:
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums: List[float]) -> None:
    # Create a helper function that will be called recursively
    def _quick_sort(items, low: int, high: int):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = _partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("list_length", type=int)
    args = ap.parse_args()

    start_list_gen_time = time()
    random_list = [random() for _ in range(args.list_length)]
    list_gen_runtime = time() - start_list_gen_time
    print(f"Generated a list of {args.list_length} floats in {list_gen_runtime}s")

    runtimes: Dict[str, float] = {}
    sort_algorithms = (
        bubble_sort,
        selection_sort,
        insertion_sort,
        heap_sort,
        merge_sort,
        quick_sort,
        sorted,
    )

    # sorted uses Timsort - https://en.wikipedia.org/wiki/Timsort - Default since 2.3
    for algo in sort_algorithms:
        copy_random_list = copy(random_list)
        # Get time after copy on purpose
        start_sort_time = time()
        algo(copy_random_list)
        runtimes[algo.__name__] = time() - start_sort_time
        del copy_random_list

    # The following does not recreate a new list list sorted()
    dot_sort_start_time = time()
    random_list.sort()
    runtimes[".sort()"] = time() - dot_sort_start_time

    print(f"\nSorting Algorithms (slowest to fastest)")
    print("- sorted() and .sort() use Timsort: https://en.wikipedia.org/wiki/Timsort")
    print("  - sorted() constructs a new list while .sort() modified the current list")
    for func_name in sorted(runtimes, key=runtimes.get, reverse=True):
        sep = "\t"
        if len(func_name) < 14:
            sep = "\t\t"
        print(f"- {func_name}:{sep}{runtimes[func_name]}s")


if __name__ == "__main__":
    sys.exit(main())
