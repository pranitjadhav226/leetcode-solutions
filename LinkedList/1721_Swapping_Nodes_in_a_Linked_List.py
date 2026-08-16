class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(k - 1):
            first = first.next

        node1 = first

        second = head
        while first.next is not None:
            first = first.next
            second = second.next

        node2 = second
        node1.val, node2.val = node2.val, node1.val

        return head
