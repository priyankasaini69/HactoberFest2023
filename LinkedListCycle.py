# linked list cycle
 def hasCycle(head):
      if head is None or head.next is None:
          return False
      slow = head
      fast = head

      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
              return True
      return False
head = [3,2,0,-4]
print(hasCycle(head))
