# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val + l2.val < 10:
            sumList = ListNode(l1.val + l2.val)
            remain = 0
        else:
            sumList = ListNode(l1.val + l2.val - 10)
            remain = 1
        tmp = sumList
        tmp1 = l1
        tmp2 = l2
        while tmp1.next != None or tmp2.next != None:
            if tmp1.next == None:
                val1 = 0
            else:
                tmp1 = tmp1.next
                val1 = tmp1.val
            if tmp2.next == None:
                val2 = 0
            else:
                tmp2 = tmp2.next
                val2 = tmp2.val
            if val1 + val2 + remain < 10:
                tmp.next = ListNode(val1 + val2 + remain)
                remain = 0
            else:
                tmp.next = ListNode(val1 + val2 + remain - 10)
                remain = 1
            # print(tmp)
            tmp = tmp.next

        if remain == 1:
            tmp.next = ListNode(remain)
            
        return sumList
            