#!/usr/bin/env swift

/*
the ever popular add two linked-lists of integers problem.

found here: 
    https://leetcode.com/problems/add-two-numbers/

I did this in Swift, because I like Swift, that said, Optionals made
this a challege for me, too much Python on the brain, my little goal 
is to make a python version of this program as well, because why not?
I also need practice in both, so if I understand one, the other should
be pretty straight forward
*/

public class ListNode {
	public var val: Int
	public var next: ListNode?
	public init() { self.val = 0; self.next = nil; }
	public init(_ val: Int) { self.val = val; self.next = nil; }
	public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
		var l1: ListNode? = l1
		var l2: ListNode? = l2

		var resultNode: ListNode? = ListNode(0)
		let headNode = resultNode

		var carryOver = 0
		while l1 != nil || l2 != nil || carryOver > 0 {
			let val1 = l1?.val ?? 0
			let val2 = l2?.val ?? 0

			let sum = val1 + val2 + carryOver
			let val = sum % 10
			carryOver = sum/10

			resultNode?.next = ListNode(val)
			resultNode = resultNode?.next
			l1 = l1?.next
			l2 = l2?.next
		}

		return headNode?.next
	}
}


let node1a = ListNode(2)
let node1b = ListNode(4)
let node1c = ListNode(3)
let node1 = node1a
node1.next = node1b
node1b.next = node1c

let node2a = ListNode(5)
let node2b = ListNode(6)
let node2c = ListNode(4)
let node2 = node2a
node2.next = node2b
node2b.next = node2c

let solution = Solution()

let solNode = solution.addTwoNumbers(node1, node2)

var newNode: ListNode?
newNode = solNode
while newNode != nil {
	if let value = newNode?.val {
		print(value)
		newNode = newNode?.next
	}
}
