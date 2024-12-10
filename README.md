# Blue_Magpie-Recognizer
- **The Final Project For Course: Introduction to Computer Vision and Its Applications.**

## 🔖 Abstract
- **台灣藍鵲 Taiwan Blue Magpie**(*Urocissa caerulea*) is the national bird of Taiwan, having striking blue plumage and a long tail.
-  However, the suspected smuggling of the **紅嘴藍鵲 Red-billed Blue Magpie** (*Urocissa erythroryncha*) into Taiwan has led to a gradual expansion of its population in recent years, which threatens the habitat of the Taiwan Blue Magpie.
-  We hope that through this project, more people will become aware of this issue and learn to recognize and distinguish between the two species.
> ![Difference](assets/difference.png)
---
- There are five kinds of blue magpies in the world:
    | Chinese Name   | English Name               |
    |----------------|----------------------------|
    | 台灣藍鵲         | Taiwan Blue Magpie         |
    | 紅嘴藍鵲         | Red-billed Blue Magpie     |
    | 黃嘴藍鵲         | Yellow-billed Blue Magpie  |
    | 白翅藍鵲         | White-winged Magpie        |
    | 斯里蘭卡藍鵲      | Sri Lanka Blue Magpie      |
- In this project, we selected three species with similar appearances: **Taiwan Blue Magpie**, **Red-billed Blue Magpie**, and **Yellow-billed Blue Magpie** as the dataset, aiming to train a model that can distinguish between them.

## 📋 TODO List
- [x] Dataset Preparation (using Selenium)
- [ ] Model Building (using PyTorch)
- [ ] Training and Evaluation (using PyTorch)
- [ ] Hyperparameter Tuning
- [ ] Model Visualization (using Captum)
- [ ] UI Wrapping (using Gradio)

## 🎬 How to Start
### Prerequisites
- Python 3.10.x
- PyTorch 2.15.x
- CUDA 11.8

### Environment Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/PuiPui32071/Blue_Magpie-Recognizer.git
    ```
2. Create a conda environment:
    ```bash
    conda create -n bmr python==3.10.15
    conda activate bmr
    ```
3. Install required packages:
    ```bash
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0  pytorch-cuda=11.8 -c pytorch -c nvidia
    conda install selenium tqdm torchinfo tensorboard ipywidgets
    conda install captum matplotlib==3.4.3 -c conda-forge
    pip install gradio
    
    conda install libpng jpeg (for macOS)
    pip install sympy==1.13.1 (if needed)
    ```
    

## 📁 Dataset Preparation
### Option 1: Use Our Dataset
- If you want to use our proposed dataset, please [click here](https://drive.google.com/drive/folders/1E_pRJGIzvn5IInmIfg55CrSge5gsOnGE?usp=drive_link) to download `dataset_1500.zip`.
- Extract `dataset_1500.zip` to the root directory.
- It contains three different types of blue magpies images, with each class having `1500` images sized `256x256`.
- We also provide `raw_images.zip` for additional sampling options.
```
├── dataset_1500
│   ├── red-billed-blue-magpie
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   ├── taiwan-blue-magpie
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   └── yellow-billed-blue-magpie
│       ├── 1.png
│       ├── 2.png
│       └── ...
```
### Option 2: Use Custom Dataset
- To run Selenium properly, you need a driver that matches your browser, eg., [Chrome](https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-tw).
- Once downloaded, place the driver in the root directory.
- Then, modify `prepare_dataset.ipynb` and run the script to get the bird dataset you want.
- Note that you must pass the [media.ebird.org](https://media.ebird.org/catalog?taxonCode=formag1&mediaType=photo) URL with the specific species to the `EbirdCrawler` class so that the crawler can work properly.
```
├── dataset_<num_of_images>
│   ├── <spicies-1>
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   ├── <spicies-2>
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   └── <spicies-3>
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   ... 
```

## 🏋️ Training
- The `pipeline.ipynb` includes all the steps to construct and train our blue magpie recognizer. Just run it and have fun.
- Additionally, you can build your own model and save it in the `models` folder. Then, you can import it in the `Build CNN Model` block and train it.

## 🧪 Testing
- To properly inspect the training details, we automatically save the TensorBoard logs in the `runs` folder and the model checkpoints in the `ckpts` folder.You can check them with TensorBoard and load the pre-trained model.

### 🌟 Acknowledgement
- Thanks to [eBird.org](https://ebird.org/home) for providing such a platform with many valuable statistics for educational purposes :).
- Special thanks to the eBird team for their continuous efforts in maintaining and updating the database.
- We also appreciate the contributions of all the bird watchers and photographers who have shared their observations and images on eBird.