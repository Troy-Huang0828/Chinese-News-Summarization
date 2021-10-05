mkdir data
mkdir output
mkdir save
cd data
wget https://www.dropbox.com/s/ttrb0wd2k74b7j2/train.jsonl?dl=1 -O train.jsonl
wget https://www.dropbox.com/s/d2d1n99m11o7ucz/public.jsonl?dl=1 -O public.jsonl
cd ..
cd save
wget https://www.dropbox.com/s/04n15fn5ihxvehn/learning_curve.json?dl=1 -O learning_curve.jsonl
mkdir rouge18
cd rouge18
wget https://www.dropbox.com/s/c8k3x4oo6znylc2/config.json?dl=1 -O config.json
wget https://www.dropbox.com/s/1q4wlc7j4g84bje/pytorch_model.bin?dl=1 -O pytorch_model.bin


