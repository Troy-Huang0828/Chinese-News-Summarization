# Discription
This is a pytorch implementation of Chinese News Summarization by fine tune mt5-small model.
# ADL21-HW3
Dataset & evaluation script for ADL 2021 homework 3
## create enviroment
```
use the requirements.txt to install the enviroment for homework3
step 1:create a new enviroment and activate it 
step 2:conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
step 3:cd path/r09921083
step 4:pip install -r requirements.txt
```

## Download model and data
```
bash download.sh
```

## create public or private submission 
```
cd path/r09921083
bas  run.sh path${1} path${2}
path${1}:input file
path${2}:output file 
```
## fine tune mt5-small
```
cd path/R09921083_HW3
bash run_finetune.sh
ps:Every epoch the finetune model will be save in a folder name "output".
```
## draw figure
```
There is a file name draw_pic.py
Run the file and it will make three figure, rouge1, rouge2 and rougeL.
```

