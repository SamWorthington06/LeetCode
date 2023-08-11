# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1 = self.reverse_function(l1)
        l2 = self.reverse_function(l2)

        int_l1 = int(''.join(str(num) for num in l1))
        int_l2 = int(''.join(str(num) for num in l2))

        sum = int_l1 + int_l2
        sum = str(sum)

        list_sum = [int(sum[num_index]) for num_index in range(len(sum))]
        list_sum.reverse()

        answer = self.convert_to_ListNode(list_sum)

        return answer
    
    def reverse_function(self, list_node):
        
        array = []

        while list_node is not None:
            array.insert(0, list_node.val)
            list_node = list_node.next

        return array
    
    def convert_to_ListNode(self, list_sum):

        for num_index in range(len(list_sum)):
            list_sum[num_index] = ListNode(list_sum[num_index])

        for num_index in range(len(list_sum)):
            if num_index == len(list_sum) - 1:
                break
            else:
                list_sum[num_index].next = list_sum[num_index + 1]

        return list_sum[0]

if __name__ == '__main__':

    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6

    solution = Solution()
    print(solution.addTwoNumbers(node1, node4))