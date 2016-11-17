class TreeNode(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class TreePrinter:

  def zig_zag(self, root):
    # normally left->right
    # But, reverse every other result list
    if root is None:
        return []

    stack = []
    stack.append(root)
    stack.append(None)
    results = []
    current_level = []
    left_to_right = True

    while len(stack) > 0:
      # O(1)
      current = stack.pop(0) 
      if current != None:
        # Add it to the current level
        current_level.append(current.val)

        # Add children to stack
        if current.left:
          stack.append(current.left) # O(1)
        if current.right:
          stack.append(current.right)

      else:
        # Add current level to response, reverse every other level
        if left_to_right:
          results.append(current_level)
          left_to_right = False
        else:
          rev = list(reversed(current_level)) # O(n)
          results.append(rev)
          left_to_right = True

        # Reset level list
        
        current_level = []
        if len(stack) > 0:
          # Append delimiter
          stack.append(None)
    return results

def test():
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)
  printer = TreePrinter()
  print printer.zig_zag(root)

test()
