import matplotlib.pyplot as plt
import numpy as np


C_T = np.arange(0, 100, 0.02)
C_F = 0.00

plt.xlabel("C_T")
plt.ylabel("C_F")

plt.plot(C_T, C_T - 30, color="r", linestyle="-", linewidth=1)
plt.plot(C_T, -0.5*C_T + 30, color="b", linestyle="-", linewidth=1)
plt.plot(C_T, 2*C_T - 20, color="g", linestyle="-", linewidth=1)
plt.plot(C_T, -4*C_T + 220, color="b", linestyle="-", linewidth=1)

plt.show()

