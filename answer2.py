from collections import defaultdict
import time
import math

class Node:
    def __init__(self, key, value, weight):
        self.key = key
        self.value = value
        self.weight = weight
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(None, None, None)  # dummy head node
        self.tail = Node(None, None, None)  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key, value, weight):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.weight = weight
            self._move_to_front(node)
        else:
            if self.size == self.capacity:
                self._evict()
            new_node = Node(key, value, weight)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            self.size += 1

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _evict(self):
        # Remove least recently used node (tail)
        node_to_remove = self.tail.prev
        del self.cache[node_to_remove.key]
        self._remove_node(node_to_remove)
        self.size -= 1

    def get_score(self, node):
        current_time = time.time()
        last_accessed_time = node.weight
        score = node.weight / (math.log(current_time - last_accessed_time + 1) + 1)
        return score
    
    
   # get(key): The average time complexity of get(key) is constant, O(1), because accessing an item in the hash map takes constant time. The doubly linked list operations involved in moving the accessed node to the front also take constant time. 
   # put(key, value, weight): The time complexity of put(key, value, weight) is also constant, O(1), on average. Adding an item to the hash map and the doubly linked list both take constant time. In the worst case scenario, when an eviction is required, the time complexity would be O(K), where K is the capacity of the cache, as we need to remove the least recently used item.
# Overall, this implementation of the cache provides efficient time complexities for both get(key) and put(key, value, weight), with an average time complexity of O(1) for both operations.