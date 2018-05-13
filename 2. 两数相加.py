"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

链表，数学
"""
from hikari_tool import ListNode, SingleLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        s = l1.val+l2.val
        head = ListNode(s % 10)
        tag = s//10  # 是否进位,0或1
        cur = head  # 新链表的工作指针
        while l1.next and l2.next:
            s = l1.next.val+l2.next.val+tag
            cur.next = ListNode(s % 10)
            tag = s//10
            l1, l2, cur = l1.next, l2.next, cur.next
        # 其中有一个链表遍历结束,将另一个链表遍历完
        while l1.next:
            s = l1.next.val+tag
            cur.next = ListNode(s % 10)
            tag = s//10
            l1, cur = l1.next, cur.next
        while l2.next:
            s = l2.next.val+tag
            cur.next = ListNode(s % 10)
            tag = s//10
            l2, cur = l2.next, cur.next
        if tag:  # 可能进位
            cur.next = ListNode(tag)
        return head

    def addTwoNumbers_2(self, l1, l2):
        # 官方答案,好简洁...
        # 结果这个用时180ms, 自己写的用时160ms...
        head = ListNode(0)  # 随意创建一个头结点,方便处理
        p = head  # 工作指针
        carry = 0  # 进位
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            carry = s//10
            p.next = ListNode(s % 10)
            p = p.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return head.next


if __name__ == '__main__':
    l1 = SingleLinkedList([8, 5])  # 代表数字58
    l2 = SingleLinkedList([7, 5])  # 代表数字57
    l3 = SingleLinkedList()
    l3.head = Solution().addTwoNumbers(l1.head, l2.head)
    l3.travel()  # [5, 1, 1], 代表数字115
    l4 = SingleLinkedList()
    l4.head = Solution().addTwoNumbers_2(l1.head, l2.head)
    l4.travel()
