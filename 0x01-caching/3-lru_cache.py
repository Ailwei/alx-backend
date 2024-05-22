#!/usr/bin/env python3
"""
LRU caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                lru_key = self.cache_keys.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            # Update the key usage order
            self.cache_keys.remove(key)
            self.cache_keys.append(key)
            return self.cache_data[key]
        else:
            return None

    def print_cache(self):
        """
        Print the cache data
        """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
