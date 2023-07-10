from concurrent.futures import ThreadPoolExecutor
import numpy as np
from functools import partial
import fast_histogram
import matplotlib.pyplot as plt

data = np.random.normal(0, 10, [2, 1000000])
workers = 4

with ThreadPoolExecutor(workers) as e:
 chunk = data.shape[1]//workers
 chunk0 = [data[0, i*chunk:(i+1)*chunk] for i in range(workers)]
 chunk1 = [data[1, i*chunk:(i+1)*chunk] for i in range(workers)]
 func = partial(fast_histogram.histogram2d, bins=200, range=((-10, 10), (-10, 10)))
 results = e.map(func, chunk0, chunk1)
 results = sum(results)

x = np.linspace(np.min(data), np.max(data), 200)
y = results[0,:]

plt.bar(x, y, color='green', width=0.7)
plt.show()
