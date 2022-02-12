x = np.linspace(-2*np.pi, 3*np.pi, 201)

k, a, b = np.linspace(2, 10, num = 3)
k1, a1, b1 = np.linspace(11, 20, num = 3)
k2, a2, b2 = np.linspace(21, 30, num = 3)

print(f'k={k}, a={a}, b={b}')
print(f'k1={k1}, a1={a1}, b1={b1}')
print(f'k2={k2}, a2={a2}, b2={b2}')

plt.figure(figsize = (10, 5))
plt.plot(x, k * np.cos(x - a) + b, label='k, a, b')
plt.plot(x, k1 * np.cos(x - a1) + b1, color='g', label='k1, a1, b1')
plt.plot(x, k2 * np.cos(x - a2) + b2, color='r', label='k2, a2, b2')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(frameon=False)
plt.show()
k=2.0, a=6.0, b=10.0
k1=11.0, a1=15.5, b1=20.0
k2=21.0, a2=25.5, b2=30.0