class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the dummy head of the list.
        dummy = ListNode(-1)

        # Set a pointer "current" to the dummy head.
        current = dummy

        while l1 and l2:
            # Choose the node with the smaller value and append it to the result.
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            # Move the pointer to the next node in the result list.
            current = current.next

        # If one of the input lists still has nodes, append all the remaining nodes to the result list.
        if l1:
            current.next = l1
        else:
            current.next = l2
        
        # The first node of the dummy list is a placeholder, so we return the next node.
        return dummy.next
