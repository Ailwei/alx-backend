#!/usr/bin/env python3
"""
certain rows are removed from the dataset,
the user does not miss items from dataset when changing page.
"""


import csv
import math
from typing import List, Dict, Optional

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a specific page of data from the dataset using index-based pagination.

        Args:
            index (int, optional): The start index of the page. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia information for the specified page.
        """
        assert index is None or (isinstance(index, int) and index >= 0), "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        total_items = len(dataset)

        # Calculate the current index and next index
        if index is None:
            current_index = 0
        else:
            current_index = index
        next_index = min(current_index + page_size, total_items)

        # Get the data for the current page
        data = dataset[current_index:next_index]

        return {
            "index": current_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
