# Measuring Error

# knob_weight = 0.5
# input = 0.5
# goal_pred = 0.8

# pred = input * knob_weight

# error = (pred - goal_pred) ** 2

# print(error)

# Hot and Cold Learning
def neural_network(input,weight):
  prediction = input * weight
  return prediction

#input
number_of_toes = [8.5]
win_or_loss_binary = [1]

input = number_of_toes[0]
true = win_or_loss_binary[0]
weight = 0.1
lr = 0.01

pred = neural_network(input, weight)

error = (pred - true) ** 2
print(error)

p_up = neural_network(input, weight + lr)
e_up = (p_up - true) ** 2
print(e_up)

p_dn = neural_network(input, weight -lr)
e_dn = (p_dn - true) ** 2
print(e_dn)

if(error > e_dn or  error > e_up):
  if(e_dn < e_up):
    weight -= lr
  if(e_up < e_dn):
    weight += lr
print(weight)


