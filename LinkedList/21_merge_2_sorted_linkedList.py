class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2

        dummy = ListNode(0)
        current = dummy

        while i is not None and j is not None:
            if i.val < j.val:
                current.next = i
                i = i.next
            else:
                current.next = j
                j = j.next

            current = current.next

        if i is not None:
            current.next = i
        else:
            current.next = j

        return dummy.next
