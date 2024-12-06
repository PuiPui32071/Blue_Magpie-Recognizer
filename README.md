# Blue_Magpie-Recognizer
The final project for course: Introduction to Computer Vision and Its Applications

## How to Start
### Prerequisites
- Python 3.9.x
- PyTorch 2.15.x
- CUDA 11.8

### Environment Setup
1. Clone this repository:
    ```
    git clone ...
    ```
2. Create a conda environment:
    ```
    conda create -name bmr python=3.9
    conda activate bmr
    ```
3. Install required packages:
    ```
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0  pytorch-cuda=11.8 -c pytorch -c nvidia
    conda install selenium matplotlib==3.3.4 tqdm
    ```
4. Download the webdriver:
    - To properly use selenium, the webdriver matched your browser is needed.
    - Once downloaded it, please place the webdriver file on the root.


## Training
### Project Structure
- not finished yet
```text
project_root/
├── dataset/
│   ├── preprocess.py
│   ├── raw/
│   ├── processed/
.   .
.
.
├── test.py
├── requirements.txt
└── main.py
```

## Testing


## TODO List
- [ ] Dataset Collection(selenium)
- [ ] Model Building
- [ ] Training and Evaluation
- [ ] Hyperparameter Tuning
- [ ] Model Visulization(captum)
- [ ] UI Wrapping(gradio)
