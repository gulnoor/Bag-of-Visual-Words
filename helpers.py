import matplotlib.pyplot as plt
import numpy as np


def showbatch(dataset):
    idx = np.random.randint(0, len(dataset) - 1, 8)
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    axes = axes.flatten()

    for i in range(8):
        img = dataset[idx[i]][0].permute(1, 2, 0)
        label = dataset.data[idx[i]][1]

        axes[i].imshow(img)
        axes[i].set_title(f"{label}")
        axes[i].axis("off")

    plt.tight_layout()
    plt.show()
