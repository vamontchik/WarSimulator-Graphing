import numpy as np
import matplotlib.pyplot as plt

def least_squares(A_fill, b_fill, degree):
  A = np.zeros((1,degree+1), dtype=np.int64)
  for val in A_fill:
    fill_list = np.array([], dtype=np.int64)
    for i in range(degree + 1): # (+1) since range start at 0
      fill_list = np.append(fill_list, val ** i)
    A = np.vstack([A, fill_list])
  A = np.delete(A, 0, 0)

  b = b_fill
  
  return np.linalg.lstsq(A, b, rcond=None)[0]

def fillList(lines):
  values = []
  percents = []
  isValue = True
  for line in lines:
    without_newline = line[:-1]
    if isValue:
      values.append(int(without_newline))
      isValue = False
    else:
      percents.append(float(without_newline))
      isValue = True
  return np.array(values), np.array(percents)

def fillPlotValues(x, x_values, degree):
  line_eval = []
  for val in x_values:
    result = 0.0
    for i in range(degree + 1):
      '''
      x[i] and (val**i) to get it to multiply coordinates with values in correct ordering
      '''
      result += x[i] * (val**i) 
    line_eval.append(result)
  return np.array(line_eval)

# setup
lowestCardValue = 6
highestCardValue = 14

f = open("save.txt", "r")
lines = f.readlines()
np_values, np_percents = fillList(lines)
x_values = np.linspace(lowestCardValue, highestCardValue, num=100)

# linear least square: linear soln
x = least_squares(np_values, np_percents, 1)
equation = "Linear Equation: " + str(x[1]) + " * x + " + str(x[0])
print(equation)
np_line_eval_linear = fillPlotValues(x, x_values, 1)

# linear least square: quadratic soln
x = least_squares(np_values, np_percents, 2)
equation = "Quadratic Equation: " + str(x[2]) + " * x^2 + " + str(x[1]) + " * x + " + str(x[0])
print(equation)
np_line_eval_quad = fillPlotValues(x, x_values, 2)

plt.scatter(np_values, np_percents, label = 'true points')
plt.plot(x_values, np_line_eval_linear, label = 'linear approximation')
plt.plot(x_values, np_line_eval_quad, label = 'quadratic approximation')
plt.legend()
plt.show()
