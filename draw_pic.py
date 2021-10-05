import json
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
with open('save/learning_curve.jsonl','r', encoding='utf-8') as file:
    data = json.load(file)

x = np.linspace(1,20,20)

rouge1=[]
rouge2=[]
rougeL = []
for i in range(len(data)):
    rouge1.append(data[i]['rouge1'])
    rouge2.append(data[i]['rouge2'])
    rougeL.append(data[i]['rougeL'])

rouge1 = np.array(rouge1)
rouge2 = np.array(rouge2)
rougeL = np.array(rougeL)


plt.title("rouge1_score")
plt.xlabel("check point")
plt.ylabel("accuracy")
plt.plot(x, rouge1)
plt.show()

plt.title("rouge2_score")
plt.xlabel("check point")
plt.ylabel("accuracy")
plt.plot(x, rouge2)
plt.show()

plt.title("rougeL_score")
plt.xlabel("check point")
plt.ylabel("accuracy")
plt.plot(x, rougeL)
plt.show()



