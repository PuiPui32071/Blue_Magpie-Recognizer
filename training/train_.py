# FILE: training/train.py
import os
import torch
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

def train_one_epoch(model, train_loader, optimizer, criterion, writer, device):
    model.train()
    running_loss = 0.0

    for images, labels in tqdm(train_loader, desc="Training"):
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    
    return running_loss / len(train_loader)

def validate_one_epoch(model, val_loader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in tqdm(val_loader, desc="Validating"):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    val_loss = running_loss / len(val_loader)
    val_acc = correct / total
    return val_loss, val_acc

def train(model, train_loader, val_loader, optimizer, criterion, save_name, device, epochs=10):
    train_loss = []
    val_loss = []
    val_acc = []
    best_val_acc = 0.0

    if not os.path.exists('ckpts'):
        os.makedirs('ckpts')

    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}/{epochs}")
        
        train_epoch_loss = train_one_epoch(model, train_loader, optimizer, criterion, device)
        train_loss.append(train_epoch_loss)
        print(f"Train Loss: {train_epoch_loss:.4f}")

        val_epoch_loss, val_epoch_acc = validate_one_epoch(model, val_loader, criterion, device)
        val_loss.append(val_epoch_loss)
        val_acc.append(val_epoch_acc)
        print(f"Val Loss: {val_epoch_loss:.4f}, Val Acc: {val_epoch_acc:.4f}")

        if val_epoch_acc > best_val_acc:
            best_val_acc = val_epoch_acc
            torch.save(model.state_dict(), f"ckpts/{save_name}.pth")
            print(f"Saved Best Model with Val Acc: {best_val_acc:.4f}")

    return train_loss, val_loss, val_acc