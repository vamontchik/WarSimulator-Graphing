import numpy as np
import matplotlib.pyplot as plt

f = open("Personal/war graphing/save.txt", "r")
lines = f.readlines()

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

np_values = np.array(values)
np_percents = np.array(percents)

# obtain x values
x_values = np.linspace(6, 14, num=100)

# linear least square: linear soln
A = np.array([
  [val, 1] for val in np_values
])
b = np_percents
x = np.linalg.lstsq(A, b, rcond=None)[0]

equation = "Linear Equation: " + str(x[0]) + " * x + " + str(x[1])
print(equation)

line_eval = []
for val in x_values:
  line_eval.append(x[0]*val + x[1])
np_line_eval_linear = np.array(line_eval)

# linear least square: quadratic soln
A = np.array([
  [val**2, val, 1] for val in np_values
])
b = np_percents
x = np.linalg.lstsq(A, b, rcond=None)[0]

equation = "Quadratic Equation: " + str(x[0]) + " * x^2 + " + str(x[1]) + " * x + " + str(x[2])
print(equation)

line_eval = []
for val in x_values:
  line_eval.append(x[0]*(val**2) + x[1]*val + x[2])
np_line_eval_quad = np.array(line_eval)

plt.scatter(np_values, np_percents, label = 'true points')
plt.plot(x_values, np_line_eval_linear, label = 'linear approximation')
plt.plot(x_values, np_line_eval_quad, label = 'quadratic approximation')
plt.legend()
plt.show()
