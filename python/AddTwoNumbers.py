# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        my_vals = { "val1": "", "val2": "" }

        def loop_linked_lists(l1=None, l2=None):
            if l1:
                my_vals["val1"] += str(l1.val)
            if l2:
                my_vals["val2"] += str(l2.val)

            if l1 and l1.next and l2 and l2.next:
                return loop_linked_lists(l1.next, l2.next)
            elif l1 and l1.next:
                return loop_linked_lists(l1.next)
            elif l2 and l2.next:
                return loop_linked_lists(None,l2.next)

        loop_linked_lists(l1, l2)

        new_val = str(int(my_vals["val1"][::-1]) + int(my_vals["val2"][::-1]))

        def generate_linked_list(new_val, new_ln=None):
            if new_val:
                parent_node = ListNode()
                parent_node.val = int(new_val[:1])
                parent_node.next = new_ln
                return generate_linked_list(new_val[1:], parent_node)
            return new_ln

        return generate_linked_list(new_val)