# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse 
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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
        carry_over = 0
        result_lst = ListNode(0)
        result_lst_curr_node = result_lst
        
        l1_curr_node = l1
        l2_curr_node = l2
        
        while l1_curr_node and l2_curr_node:
            tmp_node_val = l1_curr_node.val + l2_curr_node.val + carry_over
            if tmp_node_val >= 10:
                new_node = ListNode(tmp_node_val - 10)
                carry_over = 1
            else:
                new_node = ListNode(tmp_node_val)
                carry_over = 0
                    
            result_lst_curr_node.next = new_node
            result_lst_curr_node = new_node
            l1_curr_node = l1_curr_node.next
            l2_curr_node = l2_curr_node.next

        if l1_curr_node:
            while l1_curr_node:
                tmp_node_val = l1_curr_node.val + carry_over
                if tmp_node_val >= 10:
                    new_node = ListNode(tmp_node_val - 10)
                    carry_over = 1
                else:
                    new_node = ListNode(tmp_node_val)
                    carry_over = 0
                
                result_lst_curr_node.next = new_node
                result_lst_curr_node = new_node
                l1_curr_node = l1_curr_node.next

        if l2_curr_node:
            while l2_curr_node:
                tmp_node_val = l2_curr_node.val + carry_over
                if tmp_node_val >= 10:
                    new_node = ListNode(tmp_node_val - 10)
                    carry_over = 1
                else:
                    new_node = ListNode(tmp_node_val)
                    carry_over = 0
                
                result_lst_curr_node.next = new_node
                result_lst_curr_node = new_node
                l2_curr_node = l2_curr_node.next
                
        if carry_over == 1:
            new_node = ListNode(1)
            result_lst_curr_node.next = new_node
            result_lst_curr_node = new_node
                
        return result_lst.next