# Convolution From Scratch

This repository contains Python code for implementing convolutional neural networks (CNNs) from scratch, including the creation of a convolution layer, implementation of popular convolutional networks such as LeNet-5, and additional functionalities related to convolution operations.

## Features

- **Convolution Layer Implementation**: We provide a detailed implementation of a convolutional layer from scratch, including forward and backward propagation.
- **Convolutional Networks**: This repository includes implementations of various convolutional networks, including but not limited to LeNet-5, AlexNet, VGG, and ResNet, demonstrating how these networks can be built using basic convolutional layers.
- **Extensive Documentation**: Each component of the implementation is extensively documented to provide insights into the workings of convolutional neural networks.
- **Modular Design**: The code is structured in a modular fashion, making it easy to understand, modify, and extend for experimentation with different architectures and hyperparameters.
- **Educational Resource**: This repository serves as an educational resource for understanding the fundamentals of convolutional neural networks by implementing them from scratch.

## Contents

- `convolution_layer.py`: Implementation of a basic convolutional layer including forward and backward propagation functions.
- `lenet5.py`: Implementation of the LeNet-5 architecture using the convolutional layer.
- `alexnet.py`, `vgg.py`, `resnet.py`: Implementations of AlexNet, VGG, and ResNet architectures respectively, using the basic convolutional layer.
- `utils.py`: Utility functions used across different components of the implementation.
- `examples/`: Directory containing example scripts demonstrating the usage of different components and architectures.

## Usage

To utilize this repository, follow these steps:

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/pravincoder/convolution-from-scratch.git
    ```

2. Navigate to the cloned directory:

    ```
    cd convolution-from-scratch
    ```

3. Import the required modules in your Python scripts:

    ```python
    from convolution_layer import ConvolutionLayer
    from lenet5 import LeNet5
    # Import other architectures as needed
    ```

4. Explore the examples directory to understand how to use different components and architectures in your projects.

## Dependencies

- Python 3.x
- NumPy
- (Optional) Matplotlib (for visualization purposes in examples)
  **Note** :- All the code is done on google colab for easy access and learning.(So dependencies are not specified with caution here☺)

## Contributions

Contributions to improve the codebase, add new features, or fix bugs are welcome. Please follow the standard GitHub workflow for contributing:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your modifications and commit them (`git commit -am 'Add new feature'`).
4. Push your branch (`git push origin feature/new-feature`).
5. Create a pull request.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- The implementation in this repository is inspired by various resources and research papers in the field of convolutional neural networks.
- We acknowledge the contributions of the open-source community for providing valuable insights and resources on implementing neural networks from scratch.

## Contact

For any inquiries or feedback, please contact [Pravin Maurya](mailto:pravincoder@example.com).
To know more about me [website](https://pravincode.000webhostapp.com/)
---
