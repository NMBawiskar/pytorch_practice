import torch
import numpy as np


data = [[1,2],[2,3]]

tensor = torch.tensor(data)
print(tensor)
print(tensor.shape)
print(tensor.grad)

a = np.array([[1,2,3],[2,3,4]])
t = torch.from_numpy(a)
print(t)


random = torch.rand(size=[2,3])
print(random)
c = torch.ones_like(random)
d = torch.zeros_like(random)

e = torch.eye(5)
print(c)
print(d)

print(e)

print(e.dtype)
print(e.device)


######## operations
sum = torch.sum(c)
print(sum)

## converting tensor of single value to python object

sum_ = sum.item()
print(type(sum_), sum_)
