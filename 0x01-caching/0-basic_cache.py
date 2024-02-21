#!/usr/bin/python3
""" Class BasicCache inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item to the cache.

        Args:
            key: The key associated with the item.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache.

        Args:
            key: The key associated with the item.

        Returns:
            The item if found, otherwise None.
        """
        return self.cache_data.get(key)
