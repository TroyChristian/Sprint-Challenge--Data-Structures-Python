from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentItem = None
        self.capacityTracker = DoublyLinkedList()

    def append(self, item):
        if self.capacityTracker.length < self.capacity:
            self.capacityTracker.add_to_tail(item)
            self.currentItem = self.capacityTracker.head
        
        else:
            self.currentItem.value = item
            self.currentItem = self.currentItem.next
            if self.currentItem is None:
                self.currentItem = self.capacityTracker.head


    def get(self):
        arrayItems = []
        if self.capacityTracker.length > 0:
            newNode = self.capacityTracker.head
            while newNode:
                arrayItems.append(newNode.value)
                newNode = newNode.next
        return arrayItems


