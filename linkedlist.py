class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def setNextNode(self, node):
		self.next = node

class LinkedList:
	def __init__(self, startNode):
		self.startNode = startNode

	def insertAtEnd(self, node):
		currentNode = self.startNode
		#Get to the node that doesn't have a next (currentNode != None would go past this)
		while(currentNode.next != None):
			currentNode = currentNode.next
		currentNode.next = node

	def insertBeginning(self, node):
		temp = self.startNode
		self.startNode = node
		self.startNode.next = temp

	def removeAtEnd(self):
		currentNode = self.startNode
		previousNode = None
		while(currentNode.next != None):
			previousNode = currentNode
			currentNode = currentNode.next
		previousNode.next = None



	def removeAtBeginning(self, node):
		print(y)

	def printEachElement(self):
		currentNode = self.startNode
		#Get to the node that doesn't have a next and then go to the node that doesn't have a next (None) so that we use it
		while(currentNode != None):
			print("Data: " + str(currentNode.data) + "  Next: " + str(currentNode.next))
			currentNode = currentNode.next

v = Node(5)
w = Node(4)
x = Node(1)
y = Node(2)
z = Node(3)

x.setNextNode(y)
y.setNextNode(z)

myList = LinkedList(x)
print("Initial Linked List")
myList.printEachElement()
print("insertBeginning(Node(5))")
myList.insertBeginning(v)
myList.printEachElement()
print("insertAtEnd(Node(4))")
myList.insertAtEnd(w)
myList.printEachElement()
print("removeAtEnd()")
myList.removeAtEnd()
myList.printEachElement()
