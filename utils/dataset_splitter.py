import os
import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

class DatasetSplitter:
    def __init__(self, dataset_dir: str = 'dataset_1500', train_ratio: int = 0.7, val_ratio: int = 0.15, test_ratio: int = 0.15):
        self.dataset_dir = dataset_dir
        self.train_ratio = train_ratio
        self.val_ratio = val_ratio
        self.test_ratio = test_ratio

    def split_dataset(self):
        """
        Split the dataset into train, validation, and test sets
        """

        transform = transforms.Compose([
            transforms.ToTensor(),
        ])

        dataset = datasets.ImageFolder(root=self.dataset_dir, transform=transform)
        print(f"Dataset classes: {dataset.class_to_idx}")
        print(f"Dataset size: {len(dataset)}")

        train_ratio = int(self.train_ratio * len(dataset))
        val_ratio = int(self.val_ratio * len(dataset))
        test_ratio = int(self.test_ratio * len(dataset))
        train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_ratio, val_ratio, test_ratio])

        # train_dataset = train_dataset.dataset
        # val_dataset = val_dataset.dataset
        # test_dataset = test_dataset.dataset

        if not os.path.exists('dataset'):
            os.makedirs('dataset')

        torch.save(train_dataset, 'dataset/train_dataset.pt')
        torch.save(val_dataset, 'dataset/val_dataset.pt')
        torch.save(test_dataset, 'dataset/test_dataset.pt')

    def calc_dataset_mean_std(self):
        """
        Calculate the mean and std of the dataset
        """

        transform = transforms.Compose([
            transforms.ToTensor(),
        ])

        dataset = datasets.ImageFolder(root=self.dataset_dir, transform=transform)
        dataset_loader = DataLoader(dataset, batch_size=32, shuffle=False)

        mean = 0.0
        std = 0.0

        for images, _ in dataset_loader:
            mean += images.mean([0, 2, 3])
            std += images.std([0, 2, 3])

        mean /= len(dataset_loader)
        std /= len(dataset_loader)
        print(f"Mean: {mean}, Std: {std}")