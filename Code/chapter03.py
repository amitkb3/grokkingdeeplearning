
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

#Multi-input Multi-output Neural Network
def w_sum(a,b):
  assert(len(a) == len(b))
  output = 0
  for i in range(len(a)):
    output += a[i] * b[i]
  return output

def vect_mat_mult(vect, matrix):
  assert(len(vect) == len(matrix))
  output = [0, 0, 0]

  for i in range(len(vect)):
    output[i] = w_sum(vect, matrix[i])
  
  return output

def neural_network(input, weights):
  prediction = vect_mat_mult(input,weights)
  return prediction

#inputs
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]

weights = [[0.1, 0.1, -0.3],
           [0.1, 0.2, 0.0],
           [0.0, 1.3, 0.1] ]

pred = neural_network(input,weights)
print(pred)



