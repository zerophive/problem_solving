#!/usr/bin/env python3

# Add two link-lists of integers, this time in python
#
# found here:
#   https://leetcode.com/problems/add-two-numbers/
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultNode = ListNode(0)
        headNode = resultNode

        carryOver = 0
        while l1 or l2 or carryOver > 0:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)


            sum = val1 + val2 + carryOver
            val = sum % 10
            carryOver = sum // 10

            resultNode.next = ListNode(val)
            resultNode = resultNode.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return headNode.next

node1a = ListNode(2)
node1b = ListNode(4)
node1c = ListNode(3)
node1 = node1a
node1.next = node1b
node1b.next = node1c

node2a = ListNode(5)
node2b = ListNode(6)
node2c = ListNode(4)
node2 = node2a
node2.next = node2b
node2b.next = node2c

solution = Solution()

solNode = solution.addTwoNumbers(node1, node2)

newNode = solNode
while newNode is not None:
    print(newNode.val)
    newNode = newNode.next
