import os
import random
import torchvision.transforms as transforms
import torchvision.utils as vutils
from PIL import Image
from tqdm import tqdm

class ImageSampler:
    def __init__(self, dir: str, num_samples: int = 1500):
        self.dir = dir
        self.num_samples = num_samples
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.RandomCrop(256),
            transforms.ToTensor(),
        ])

    def sample_images(self):
        """
        Random sampe and save images from the directory
        """

        for class_name in os.listdir(self.dir):
            img_extentions = ['jpg', 'jpeg', 'png']
            images_paths = []

            for root, dirs, files in os.walk(os.path.join(self.dir, class_name)):
                for file in files:
                    if file.endswith(tuple(img_extentions)):
                        # check if the image is valid
                        try:
                            with Image.open(os.path.join(root, file)) as img:
                                img.verify()
                            images_paths.append(os.path.join(root, file))
                        except:
                            # print(f"invalid image: {os.path.join(root, file)}")
                            pass

                images_paths = random.sample(images_paths, self.num_samples)

                if not os.path.exists(f"dataset_{self.num_samples}/{class_name}"):
                    os.makedirs(f"dataset_{self.num_samples}/{class_name}", exist_ok=True)
                
                for i, img_path in tqdm(enumerate(images_paths)):
                    img = Image.open(img_path)
                    img = self.transform(img)
                    vutils.save_image(img, f"dataset_{self.num_samples}/{class_name}/{str(i + 1).zfill(4)}.png")