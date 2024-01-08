# Ultrasound-guided-needle-tracking-with-deep-learning


## Prerequisites
For duplicating the environment used in this project use the following commands
```
conda create -n needle python=3.10 -y
conda activate needle
pip install -r requirements.txt
```
## Datasets
The datasets used for this study can be downloaded from the following link: https://doi.org/10.17605/OSF.IO/7DMQ4.
Unzip osfstorage-archive.zip, and move the contents to data/ folder.

## Training
For training the model use the python script
```
python Train_UIUNet.py

```
## Testing
For testing the model use the python script
```
python Test_UIUNet.py

```
