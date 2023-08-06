#!/usr/bin/env python3
'''This is a module'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFOCache class
    '''
    def __init__(self):
        '''An init function'''
        self.arr = []
        super().__init__()

    def put(self, key, item):
        '''
        put key in cache
        '''
        if (key is not None and item is not None):
            # maintain length of cache
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                # check if key exists, remove from stack if true.
                if (key in self.cache_data):
                    self.arr.pop(self.arr.index(key))

                self.arr.insert(0, key)  # add to top of stack
                self.cache_data[key] = item
            else:
                # check if key exists, if true remove from stack
                if (key in self.cache_data):
                    self.arr.pop(self.arr.index(key))

                else:
                    # remove key from top of stack (LIFO)
                    removed_key = self.arr.pop(0)
                    del self.cache_data[removed_key]
                    print(f'DISCARD: {removed_key}')

                # replacement policy
                self.arr.insert(0, key)
                self.cache_data[key] = item

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        '''
        return self.cache_data.get(key)
