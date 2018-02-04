from matplotlib import pyplot as plt

y_fact = []
y_exp = []
x = range(1, 5)
v_fact = 1
v_exp = 1
y_exp.append(v_exp)
for i in x:
    v_fact *= i
    v_exp *= 2
    y_fact.append(v_fact)
    y_exp.append(v_exp)

# normalize list to the same dimension
y_exp.pop()

plt.figure(figsize=(10, 6))
plt.xlabel('n')
plt.ylabel('number of operations (ns)')
plt.plot(x, y_fact, label='n!', color='red')
plt.plot(x, y_exp, label='2^n', color='blue')
plt.grid()

plt.legend()
plt.show()