# -*- coding: utf-8 -*-
import unittest

def remove_duplicates(head):
  prev_element = head
  next_element = head.next
  elements = [head.data]
  while next_element is not None:
    if next_element.data in elements:
      if next_element.next is None:
        prev_element.next = None
        next_element = None
      else:
        prev_element.next = next_element.next
        next_element = prev_element.next
    else:
      elements.append(next_element.data)
      prev_element = next_element
      next_element = next_element.next






class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates(head)
    head = Node(1,Node(3,Node(3,None)))
    remove_duplicates(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)


unittest.main()
