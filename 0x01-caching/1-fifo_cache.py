#!/usr/bin/env python3
"""
FIFO caching system
"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)

    def print_cache(self):
        """
        Print the cache data
        """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
