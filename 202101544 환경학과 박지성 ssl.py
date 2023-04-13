#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0


    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1


    def delete(self):
        pop_data = self.current.data
        if self.current is self.tail:
            self.tail = self.before
        else:
            self.before.next = self.current.next
            self.current = self.before 
            self.num_of_data -= 1
            return pop_data


    def first(self):
        if self.num_of_data == 0: 
            return None
        self.before = self.head
        self.current = self.head.next
        return self.current.data


    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next
        return self.current.data


    def size(self):
        return self.num_of_data

    def traverse_all(self):
        self.first()
        head = self.head.data
        print(head, end="")
        for _ in range(self.num_of_data):
            data = self.current.data
            self.next()
            print("-> (", data, ")", end="")
        print("-> null")


    def insert_at(self, position, new_data):
        new = Node(new_data)
        self.first()
        if position <= 0:
            print("error!")
        elif position >= self.size()+1:
                    self.append(new_data)
        else:
            for _ in range(position-1):
                self.next()
            self.current = new
            self.current.next = self.before.next
            self.before.next = new
            self.num_of_data += 1

    def remove(self,key):
        if self.head is None:
            return None       
        else:
            n = self.size()
            self.first()
            for i in range(n-1):
                value = self.current.data
                if value == key:
                    self.delete()
                    print("%d번째 원소(%d)를 삭제합니다."%(i,key))
                    self.next()
                else:
                    self.next()
            if self.size() == n:
                print("해당하는 원소가 없습니다.")

