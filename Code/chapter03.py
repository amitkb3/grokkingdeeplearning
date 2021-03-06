
# One input neural network
# def neural_network(input, weight):
#   prediction = input * weight
#   return prediction

# weight = 0.1
# number_of_toes = [8.5,9.5,10,9]
# input = number_of_toes[0]

# pred = neural_network(input,weight)
# print(pred)

# # Multi Input Neural Network

# def w_sum(a,b):
#   assert(len(a) == len(b))
#   output = 0
#   for i in range(len(a)):
#     output += (a[i] * b[i])
#   return output

# def neural_network(input,weights):
#   prediction = w_sum(input,weights)
#   return prediction

# #inputs
# toes = [8.5,9.5,9.9,9.0]
# wlrec = [0.65,0.8,0.8,0.9]
# nfans = [1.2,1.3,0.5,1.0]

# input = [toes[0], wlrec[0], nfans[0]]
# weights = [0.1, 0.2, 0]

# pred = neural_network(input,weights)
# print(pred)

# # Multi-input Numpy Version neural network
# import numpy as np

# def neural_network(input, weights):
#   prediction = input.dot(weights)
#   return prediction

# #inputs
# toes = np.array([8.5, 9.5, 9.9, 9.0])
# wlrec = np.array([0.65, 0.8, 0.8, 0.9])
# nfans = np.array([1.2, 1.3, 0.5, 1.0])

# input = np.array([toes[0], wlrec[0], nfans[0]])
# weights = np.array([0.1, 0.2, 0])

# pred = neural_network(input,weights)
# print(pred)

#Single input multiple output neural network
# def ele_mul(number, vector):
#   output = [0,0,0]
#   assert(len(output) == len(vector))

#   for i in range(len(vector)):
#     output[i] = number * vector[i]
  
#   return output

# def neural_network(input, weights):
#   prediction = ele_mul(input,weights)
#   return prediction

# #input
# wlrec = [0.65, 0.8, 0.8, 0.9]
# input = wlrec[0]
# weights = [0.3, 0.2, 0.9]

# pred = neural_network(input,weights)
# print(pred)  

# #Multi-input Multi-output Neural Network
# def w_sum(a,b):
#   assert(len(a) == len(b))
#   output = 0
#   for i in range(len(a)):
#     output += a[i] * b[i]
#   return output

# def vect_mat_mult(vect, matrix):
#   assert(len(vect) == len(matrix))
#   output = [0, 0, 0]

#   for i in range(len(vect)):
#     output[i] = w_sum(vect, matrix[i])
  
#   return output

# def neural_network(input, weights):
#   prediction = vect_mat_mult(input,weights)
#   return prediction

# #inputs
# toes = [8.5, 9.5, 9.9, 9.0]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]

# input = [toes[0], wlrec[0], nfans[0]]

# weights = [[0.1, 0.1, -0.3],
#            [0.1, 0.2, 0.0],
#            [0.0, 1.3, 0.1] ]

# pred = neural_network(input,weights)
# print(pred)

# #Stacked neural network
# def w_sum(a,b):
#   assert(len(a) == len(b))
#   output = 0
#   for i in range(len(a)):
#     output += a[i] * b[i]
#   return output

# def vect_mat_mult(vect, matrix):
#   assert(len(vect) == len(matrix))
#   output = [0, 0, 0]

#   for i in range(len(vect)):
#     output[i] = w_sum(vect, matrix[i])
  
#   return output

# def neural_network(input, weights):
#   hid = vect_mat_mult(input, weights[0])
#   prediction = vect_mat_mult(hid,weights[1])
#   return prediction

# #inputs
# toes = [8.5, 9.5, 9.9, 9.0]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]

# input = [toes[0], wlrec[0], nfans[0]]

# ih_wgt  = [[0.1, 0.2, -0.1],
#            [-0.1, 0.1, 0.9],
#            [0.1, 0.4, 0.1] ]

# hp_wgt  = [[0.3, 1.1, -0.3],
#            [0.1, 0.2, 0.0],
#            [0.0, 1.3, 0.1] ]

# weights = [ih_wgt, hp_wgt]

# pred = neural_network(input,weights)
# print(pred)

#Numpy version - Stacked Neural Network
# import numpy as np

# def neural_network(input, weights):
#   hid = input.dot(weights[0])
#   prediction = hid.dot(weights[1])
#   return prediction

# #toes #% win # fans
# ih_wgt = np.array([
#           [0.1, 0.2, -0.1], #hid[0]
#           [-0.1, 0.1, 0.9], #hid[1]
#           [0.1, 0.4, 0.1]]) #hid[2]

# hp_wgt = np.array([
#           [0.3, 1.1, -0.3], # hurt?
#           [0.1, 0.2, 0.0], # win ?
#           [0.0, 1.3, 0.1]]) # sad ?

# weights = [ih_wgt, hp_wgt]

# #inputs
# toes = np.array([8.5, 9.5, 9.9, 9.0])
# wlrec = np.array([0.65, 0.8, 0.8, 0.9])
# nfans = np.array([1.2, 1.3, 0.5, 1.0])

# input = np.array([toes[0], wlrec[0], nfans[0]])

# pred = neural_network(input,weights)
# print(pred)

#Basic primer on Numpy
import numpy as np

# a = np.array([0,1,2,3])
# b = np.array([4,5,6,7])
# c= np.array([[0,1,2,3],
#              [4,5,6,7]])
# d = np.zeros((2,4))
# e = np.random.rand(2,5)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# print(a * 0.1)
# print(c * 0.2)
# print(a * b)
# print(a * b * 0.2)
# print(a * c)
# print( a * e)

# a = np.zeros((1,4))
# b = np.zeros((4,3))

# c = a.dot(b)
# print(c.shape)

a = np.zeros((2,4))
b = np.zeros((4,3))
c = a.dot(b)
print(c.shape)

e = np.zeros((2,1))
f = np.zeros((1,3))

g = e.dot(f)
print(g.shape)

h = np.zeros((5,4)).T
i = np.zeros((5,6))

j = h.dot(i)
print(j.shape)

h = np.zeros((5,4))
i = np.zeros((5,6))

j = h.dot(i)
print(j.shape)








