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
cooper-mbp1:interview_coding cooper$ python3 sorting/sorting.py 1469
Generated a list of 1469 floats in 0.00016999244689941406s

Sorting Algorithms (slowest to fastest):
- bubble_sort:		0.2720770835876465s
- insertion_sort:	0.08428597450256348s
- selection_sort:	0.0706028938293457s
- heap_sort:		0.006710052490234375s
- merge_sort:		0.0056209564208984375s
- quick_sort:		0.002576112747192383s
- sorted:		0.00012230873107910156s
- .sort():		0.00011515617370605469s
```
