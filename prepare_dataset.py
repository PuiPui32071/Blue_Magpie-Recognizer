from utils.image_sampler import ImageSampler
from utils.dataset_splitter import DatasetSplitter

if __name__ == '__main__':
    dir = 'raw_images'
    num_samples = 1500
    image_sampler = ImageSampler(dir, num_samples)
    image_sampler.sample_images()

    dataset_dir = f'dataset_{num_samples}'
    dataset_splitter = DatasetSplitter(dataset_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15)
    dataset_splitter.calc_dataset_mean_std()
    dataset_splitter.split_dataset()