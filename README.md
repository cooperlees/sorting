# sorting

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Implementations of sorting algorithms in Python

Implementations "borrowed" from this excelent article: https://stackabuse.com/sorting-algorithms-in-python/

## Usage
```
cooper-mbp1:interview_coding cooper$ python3 sorting/sorting.py
usage: sorting.py [-h] list_length
sorting.py: error: the following arguments are required: list_length
```

- `list_length`: Integer length of the list of random floats to sort

```
cooper-mbp1:sorting cooper$ python3 sorting.py 1469
Generated a list of 1469 floats in 0.0001499652862548828s

Sorting Algorithms (slowest to fastest)
# sorted() and .sort() use Timsort: https://en.wikipedia.org/wiki/Timsort
# sorted() constructs a new list while .sort() modifies the current list

- bubble_sort:		0.29520320892333984s
- insertion_sort:	0.08135485649108887s
- selection_sort:	0.07391071319580078s
- heap_sort:		0.0062999725341796875s
- merge_sort:		0.004397869110107422s
- quick_sort:		0.002928018569946289s
- sorted:		0.0002429485321044922s
- .sort():		0.00018596649169921875s
```
