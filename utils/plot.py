import random
import torch
import torch.nn.functional as F
from torchvision import transforms
import numpy as np
import matplotlib.pyplot as plt

def plot_single(image, label, label_map, mean, std,):
    """
    Display image from model
    """
    idx = random.randint(0, len(image))

    denormalize = transforms.Normalize(
        mean=[-m/s for m, s in zip(mean, std)],
        std=[1/s for s in std]
    )

    image = denormalize(image)
    npimg = image[idx].permute(1, 2, 0).numpy()
    npimg = np.clip(npimg, 0, 1)
    
    plt.imshow(npimg)
    plt.axis('off')
    plt.title(
        f"label: {label_map[label[idx].item()]}"
    )
    plt.show()

def plot_batch(images, labels, label_map, mean, std, nrow=8):
    """
    Display a batch of images from model using subplots
    """
    denormalize = transforms.Normalize(
        mean=[-m/s for m, s in zip(mean, std)],
        std=[1/s for s in std]
    )

    images = denormalize(images)
    npimgs = images.permute(0, 2, 3, 1).numpy()
    npimgs = np.clip(npimgs, 0, 1)

    ncol = (len(images) + nrow - 1) // nrow
    fig, axes = plt.subplots(nrow, ncol, figsize=(15, 35))
    axes = axes.flatten()

    for idx, ax in enumerate(axes):
        if idx >= len(images):
            ax.axis('off')
            continue

        ax.imshow(npimgs[idx])
        ax.axis('off')
        ax.set_title(
            f"label: {label_map[labels[idx].item()]}"
        )
    plt.show()


def plot_single_pred(model, image, label, label_map, mean, std, device):
    """
    Display image and predictions from model
    """
    idx = random.randint(0, len(image))

    pred, prob = get_pred_prob(model, image, idx, device)
    denormalize = transforms.Normalize(
        mean=[-m/s for m, s in zip(mean, std)],
        std=[1/s for s in std]
    )

    image = denormalize(image)
    npimg = image[idx].permute(1, 2, 0).numpy()
    npimg = np.clip(npimg, 0, 1)
    
    plt.imshow(npimg)
    plt.axis('off')
    plt.title(
        f"{label_map[pred]}: {prob * 100:.2f}%\n(label: {label_map[label[idx].item()]})"
    )
    plt.show()

def plot_batch_pred(model, images, labels, label_map, mean, std, device, nrow=8):
    """
    Display a batch of images and predictions from model using subplots
    """
    denormalize = transforms.Normalize(
        mean=[-m/s for m, s in zip(mean, std)],
        std=[1/s for s in std]
    )

    images = denormalize(images)
    npimgs = images.permute(0, 2, 3, 1).numpy()
    npimgs = np.clip(npimgs, 0, 1)

    ncol = (len(images) + nrow - 1) // nrow
    fig, axes = plt.subplots(nrow, ncol, figsize=(15, 35))
    axes = axes.flatten()

    for idx, ax in enumerate(axes):
        if idx >= len(images):
            ax.axis('off')
            continue

        pred, prob = get_pred_prob(model, images, idx, device)
        ax.imshow(npimgs[idx])
        ax.axis('off')
        ax.set_title(
            f"{label_map[pred]}: {prob * 100:.2f}%\n(label: {label_map[labels[idx].item()]})"
        )
    plt.show()

def get_pred_prob(model, images, idx, device):
    """
    Get prediction and probability from model
    """
    model.eval()
    outputs = model(images.to(device))

    outputs = F.softmax(outputs, 1)
    max_probs, preds = torch.max(outputs, 1)
    
    # _, preds = torch.max(outputs, 1)
    # probs = F.softmax(outputs, 1)
    # max_probs, _ = torch.max(probs, 1)
    
    return preds[idx].item(), max_probs[idx].item()