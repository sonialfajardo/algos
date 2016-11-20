# Binary tree by level:
# For each level, add a delimeter to know where the current level ends.
# When I there's a "None", print and add a None at end of list.
# Simulates a queue FIFO

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def level_order(self, root):
    	if root is None:
            return []

    	# Temp list that will keep nodes in order with delimeter
    	temp_list = []
    	temp_list.append(root)
    	temp_list.append(None)
    	
    	# Use if need to return a list
    	results = []
    	result_current = []

    	while len(temp_list) > 0:
            current_node = temp_list.pop(0)

            if (current_node != None):
                print current_node.val,

                # Get children in queue
                if (current_node.left):
                	temp_list.append(current_node.left)
                if (current_node.right):
                	temp_list.append(current_node.right)
            else:    			
            	# Print newline to start a new level
            	print 
            	if (len(temp_list) > 0):
                    result_current = []
                    temp_list.append(None)

    	return results


# Driver Program to test above function
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(1)
root.right.right.right = TreeNode(8)
 
print "Level Order Traversal of binary tree is:"
solution = Solution()
solution.level_order(root)
