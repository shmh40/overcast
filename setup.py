from setuptools import setup, find_packages

setup(
    name="overcast",
    version="0.0.0",
    description="Scalable Sensitivty and Uncertainty Analyses for Causal-Effect Estimates of Continuous Valued Interventions",
    long_description_content_type="text/markdown",
    url="anon",
    author="anon",
    author_email="anon",
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=[
        "click==8.0.4",
        "torch==1.10.0",
        "numpy==1.21.2",
        "scipy==1.7.1",
        "pandas==1.3.4",
        "seaborn==0.11.2",
        "ray[tune]==1.7",
        "ray[default]==1.7",
        "hpbandster==0.7.4",
        "matplotlib==3.4.3",
        "tensorboard==2.7.0",
        "ConfigSpace==0.4.20",
        "torchvision==0.11.1",
        "scikit-learn==0.24.2",
        "pytorch-ignite==0.4.7",
    ],
    entry_points={"console_scripts": ["overcast=overcast.main:cli"],},
)
