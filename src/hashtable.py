# '''
# Linked List hash table key/value pair
# '''

#SEE PERSONAL HASHTABLE
# Assignment
# Your assignment is to implement a hash table in Python. You should be able to insert, read,
# and delete elements and handle hash collisions with linked list chaining.
# You should be able to insert an arbitrary amount of elements into your hash table,
# regardless of storage_buckets size, and read them back without any data loss.
# You should also implement a resizing function that doubles the size of your hash table
# and copies all elements into the new data structure.
#
# Run your code by typing python hashtable.py.
#
# Run tests by typing python test_hashtable.py.
#
# STRETCH GOALS
#
# Research and implement the DJB2 hashing algorithm.
#
# Update your HashTable to automatically double in size when it grows past a load factor of 0.7
# and half in size when it shrinks past a load factor of 0.2.
# This should only occur if the HashTable has been resized past the initial size.
# Refactor tests to pass with your resizing HashTable.
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage_buckets = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage_buckets capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''
        # Step 1 increase size
        self.size += 1

        # 2 compute index of key
        index = self._hash_mod(key)

        # Go to the node corresponding to the hash
        lp = self.storage_buckets[index]
        # 3. If bucket is empty:
        if lp is None:
            # Create LinkedPair, add it, return
            self.storage_buckets[index] = LinkedPair(key, value)
            return
        # 4. Iterate to the end of the linked list at provided index
        prev = lp
        while lp is not None:
            prev = lp
            lp = lp.next
        # Add a new LinkedPair at the end of the list with provided key/value
        prev.next = LinkedPair(key, value)




    def remove(self, key):
        # 1. Compute hash
        index = self._hash_mod(key)
        node = self.storage_buckets[index]
        prev = None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
            # 4. The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.storage_buckets[index] = node.next  # May be None, or the next match
            else:
                prev.next = prev.next.next  # LinkedList delete by skipping over
            # Return the deleted result
            return result


    def retrieve(self, key):
        # 1. Compute hash
        index = self._hash_mod(key)
        # 2. Go to first node in list at bucket
        node = self.storage_buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''

        # use when trying to insert when an array is full
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.size):
            new_storage[i] = self.storage_buckets[i]

        self.storage_buckets = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("inserted")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage_buckets)
    ht.resize()
    new_capacity = len(ht.storage_buckets)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    #
    # print("")
