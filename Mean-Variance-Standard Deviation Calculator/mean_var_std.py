import numpy as np

def calculate(m):
  if len(m) != 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.array(m)
  b = arr.reshape(3, 3)
  calculations = {
    'mean' : [b.mean(axis=0).tolist(), b.mean(axis=1).tolist(), b.mean()],
    'variance' : [b.var(axis=0).tolist(), b.var(axis=1).tolist(), b.var()],
    'standard deviation' : [b.std(axis=0).tolist(), b.std(axis=1).tolist(), b.std()],
    'max' : [b.max(axis=0).tolist(), b.max(axis=1).tolist(), b.max()],
    'min' : [b.min(axis=0).tolist(), b.min(axis=1).tolist(), b.min()],
    'sum' : [b.sum(axis=0).tolist(), b.sum(axis=1).tolist(), b.sum()]
  }


  return calculations