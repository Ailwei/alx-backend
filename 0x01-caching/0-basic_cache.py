#!/usr/bin/env python3
"""
Basic caching system
"""


class BaseCaching:
    """
    Base class for caching systems
    """

    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialize the cache
        """
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        raise NotImplementedError(
                "put must be implemented in your cache class"
                )

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)


class BasicCache(BaseCaching):
    """
    Basic caching system without limit
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
