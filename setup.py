from setuptools import setup, find_packages

setup(
    name="torch_points3d",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.2.0",
        "torch-geometric>=2.5.0",
        "torch-scatter>=2.1.2",
        "torch-sparse>=0.6.18",
        "torch-cluster>=1.6.3",
        "pytorch_metric_learning>=0.9.87",
        "hydra-core>=1.0.0",
        "wandb>=0.8.18",
        "matplotlib>=3.1",
        "torchnet>=0.0.4",
        "scikit-image>=0.16.2",
        "numba>=0.60.0",
        "plyfile>=0.7.2",
        "tqdm>=4.40",
        "tensorboard>=2.1",
        "gdown>=3.12.0",
    ],
    python_requires='>=3.12',
)
