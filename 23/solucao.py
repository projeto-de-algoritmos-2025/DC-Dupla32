import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []

        for i, head in enumerate(lists):
            if head:  
                heapq.heappush(min_heap, (head.val, i, head))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, list_index, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))

        return dummy.next