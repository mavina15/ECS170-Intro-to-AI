# ECS 170: Introduction to Artificial Intelligence

Welcome to the ECS 170 repository for the Introduction to Artificial Intelligence course! This repository contains the final project, as well as the `h1` and `h2` files.

## Final Project

The final project in this repository represents the culmination of your efforts and understanding of AI concepts covered in the course. The project is designed to showcase your ability to apply various AI techniques to solve real-world problems. 

### Project Structure

- **`/src`:** This directory contains the source code for your final project. It's organized into logical modules or components, and the main implementation files are typically found here.

- **`/data`:** If your project involves data, this directory is where you store it. Include any necessary datasets, and provide a brief description of the data and its format.

- **`/docs`:** Any documentation related to your project can be found here. This may include a project report, algorithm explanations, or any other relevant documentation.

- **`/tests`:** If applicable, include any test cases or unit tests for your project.

### Running the Project

Provide clear instructions on how to run and test your project. Include dependencies, setup steps, and any other information necessary for someone to replicate your results.

## H1 and H2 Files

### H1: [File Name]

This file represents the first homework assignment for the course. It typically covers foundational concepts and exercises related to the early topics discussed in the course.

### H2: [File Name]

This file represents the second homework assignment for the course. It may cover more advanced topics or extend the concepts learned in the first homework.

## Contributing

If you have any improvements or suggestions for the repository, feel free to open an issue or submit a pull request. Collaboration is encouraged!

Happy coding and best of luck with your AI endeavors!


# ECS 170: Introduction to Artificial Intelligence

Welcome to the ECS 170 repository for the Introduction to Artificial Intelligence course! This repository contains three significant components: Homework 1 (H1) - "Solve 15 Puzzle using A* Search," Homework 2 (H2) - "Constructing an Image Classifier using a CNN," and the Final Project - "Enhancing Network Anomaly Detection."

## Homework 1: Solve 15 Puzzle using A* Search

The H1 file in this repository represents the first homework assignment, where the task is to solve the classic 15 Puzzle using the A* search algorithm. The assignment likely involves implementing the A* algorithm, creating heuristics, and solving instances of the 15 Puzzle.

### File Structure
- **`/src`:** This directory contains the source code for solving the 15 Puzzle using the A* search algorithm.
- **`/docs`:** Any documentation related to the homework assignment can be found here, including explanations of the implemented algorithms and heuristics.

### How to Run
Include clear instructions on how to run the code, specifying any dependencies or setup steps necessary.

## Homework 2: Constructing an Image Classifier using a CNN
Homework 2 - Fashion MNIST Image Classification

## Overview
This repository contains the implementation of a Convolutional Neural Network (CNN) using TensorFlow and Keras for classifying images in the Fashion MNIST dataset. The goal is to create a robust model capable of distinguishing between different fashion items.

## Part 1: Analyzing the Data
### Libraries
- TensorFlow and Keras for deep learning
- Matplotlib for visualizing images
- NumPy for array manipulation
- Scikit-learn for confusion matrix visualization

### Loading and Splitting Data
The Fashion MNIST dataset is loaded and split into training and testing sets. The dataset consists of 70,000 images, with 60,000 used for training and 10,000 for testing. There are 10 categories, including T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, and Ankle boot.

## Part 2: Training the Model
### CNN Architecture
The CNN is built with:
- 2 Convolutional layers
- 2 Max Pooling layers
- 2 Fully Connected layers
- Softmax layer with 10 nodes for the 10 categories

### Compiling the Model
The model is compiled with the Adam optimizer, sparse categorical crossentropy loss, and sparse categorical accuracy metric. The model summary is displayed.

### Training the Model
The model is trained for 10 epochs using the Fashion MNIST training data.

### Saving the Model
The trained model is saved to a file named 'model.h5'.

### Plotting Training and Loss Functions
Accuracy and loss functions are plotted against epochs to visualize model performance during training.

## Part 3: Prediction
### Evaluating on Test Data
The model is evaluated on the test data, and the test accuracy is printed.

### Confusion Matrix
A confusion matrix is generated and displayed to assess the model's performance across different categories.

### Visualizing Random Predictions
Random predictions made by the model on a subset of test images are visualized, showing predicted labels, true labels, and the correctness of predictions.

## Part 4: Conclusion
The project demonstrates the creation, training, and evaluation of a CNN model for the Fashion MNIST dataset. It showcases the use of TensorFlow and Keras for deep learning tasks, provides insights into model performance through visualizations, and highlights areas where the model may encounter challenges. Overall, it serves as a practical example of image classification using deep learning techniques.


## Final Project: Enhancing Network Anomaly Detection

The Final Project in this repository focuses on enhancing network anomaly detection. This project likely involves applying various AI techniques to improve the accuracy and efficiency of network anomaly detection systems.

### Project Structure
- **`/src`:** This directory contains the source code for enhancing network anomaly detection.
- **`/data`:** Datasets or any relevant data files required for the project.
- **`/docs`:** Project documentation, including a report, explanations of applied techniques, and results.

### Running the Project
Provide clear instructions on how to run and test the enhanced network anomaly detection code, specifying any dependencies or setup steps.

## Contributing

Feel free to contribute improvements or suggestions for this repository. Open issues or submit pull requests to collaborate on making this resource even more valuable.

Good luck with your AI endeavors!
