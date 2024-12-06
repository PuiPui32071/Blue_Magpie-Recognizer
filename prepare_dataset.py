from utils.image_sampler import ImageSampler

if __name__ == '__main__':
    dir = 'raw_images'
    num_samples = 1500
    image_sampler = ImageSampler(dir, num_samples)
    image_sampler.sample_images()