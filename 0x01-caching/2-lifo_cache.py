#!/usr/bin/env python3
"""
LIFO caching system
"""

BasicCache = __import__('basic_cache').BasicCache


class LIFOCache(BaseCaching):
    """
    LIFO caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the last inserted key
                last_key = list(self.cache_data.keys())[-2]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

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
