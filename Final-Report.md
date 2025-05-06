# Skull-Scan

## Heading
Project Name - Skull-Scan 

Team Name - The Boneheads

Team Members - Mylon Jones, Ryan Trenner, Scott Gibson

## Introduction

### The Project:
The Skull-Scan software uses a machine learning model trained on images from the BodyFarm database. It is trained to classify an input image of a head, and estimate the level of decay of the subject in the image. The software has a user friendly web interface that is simple and easy to use.

### The Motivation:
The motivation for this project is to create a tool that might be useful for administrators sorting unlabeled images at the BodyFarm. This project could help database administrators by estimating the stage of decay, thus allowing the to use the data even if they do not know the exact details of when the picture was taken. Another point of motivation behind this project was potential utility for forensic investigation. This project could be a proof of concept for the use of AI image classification for guessing the time of death.

### The Approach:
The approach taken in this project starts with using an existing pre-trained model and fine-tuning it using images of heads at different stages of decay from the BodyFarm database, then using the fine-tuned model to classify any uploaded skull image into one of the stages of decay.

### The Changes:


### Results and Conclusions:


## Customer Value

### The Changes:


## The Technology

### Architecture:

The software for this project runs on a Docker container on a remote machine. The Docker container contains the environment and dependencies necessary to fine-tune models and run classification tasks. The container has the user home directory from the remote machine mounted to allow for convenient transfer of files between the machine and container. Port 5023 is forwarded from the container to the machine to facilitate access to the web interface through ssh.

The software used to handle models, image data and fine-tuning came from the Hugging Face ecosystem. Hugging Face is platform for sharing and finding machine learning models and data sets. They have open source software for interacting with their online repositories and using models and data sets. The code for this project was directly inspired from the image classification example in the Hugging Face Transformers repository. The library provides a user friendly way to load and split data, download models, fine-tune models, and run tasks such as image classification with those models. The most critical part of the library for the purposes of this project is the Trainer class which takes in the model, the data set, the image processor, and the collate function and other configurations. This class automates the fine-tuning which this project uses with the body farm data to classify images.
(url)[https://huggingface.co/]

The web interface.

### Changes:

Because the initial technology description was very general, in summary it said the major technology for this project would be AI models and Python, there were no changes to the technology choice. However, the specific technology used did evolve throughout development. Initially the image recognition tool was going to be CLIP by OpenAI. CLIP is also an image classification library, but it was not clear how to use it to train a model with the database data or if that was even a possibility. The CLIP readme file mentioned Hugging Face, which ended up being a better choice for this project. It was also determined that using Docker would be superior and more convenient than running the software directly on the remote machine.

### Testing and Results:
After testing several models (Swin Transformer, DieT, Baseline CNN), we selected ConvNext as the final model due to its overall strongest performance across all stages of decomposition. The model was fine tuned on a labeled dataset from the BodyFarm, using an 85/15 train-validation split. 

Here is a summary of classification accuracy across decompositon stages: 

| Stage | True Group | ConvNeXt Accuracy | Notes                                                                                                  |
| ----- | ---------- | ----------------- | ------------------------------------------------------------------------------------------------------ |
| 1     | group1     | **99.2%**         | Correct                                                                                                |
| 2     | group1     | **76.8%**         | Correct, but lower than Stage 1 due to overlap between early decomposition stages                      |
| 3     | group2     | **92.5%**         | Correct                                                                                                |
| 4     | group3     | **60%**           | Incorrect — most predictions were group2, indicating difficulty distinguishing mid-stage decomposition |
| 5     | group3     | **96.5%**         | Correct                                                                                                |
| 6     | group4     | **58%**           | Incorrect — commonly confused with group3                                                              |


Overall Performance highlights
* ConvNext outperformed other models on early and late decomposition stages, making it a strong candidate for real-world application.
* Mid-stages remain challenging, likely due to visual similarity in features between neighboring classes
* Average accuracy across all stages: approximately 80.5%
    

## Team

### Participation:
While at first member activity was rather weak and participation was intermittent, by the end of the project all team members were on board and fully active.

### Role Changes:
Member roles changed throughout the development of the project just like the goals and deliverables of the project changed. The team members had to take on and swap out roles to accommodate for the changes in project trajectory.

  * Ryan Trenner: User Interface, Scripting, Research
  * Mylon Jones: Management, Research, Proof of Concept
  * Scott Gibson: Testing, Research, Debugging

## Project Management

### Goals Met
The fundamental goals for this project were met. Namely, the software is successfully and accurately able to make classifications about stage of decomposition based on image input. The software is also sufficiently modular so it would be easy to add and test additional features. 

### Goals Deferred

  * Inspiration for Continued Development

Right now this project simply classifies an image into to a set of classes that indicate the stage of decomposition, but originally there were going to be many other features. The other features included classifying age at death, the sex of the subject, and the identity of the subject. Subject identification being an especially desirable achievement. If development were to move forward, determining subject identity would be the preeminent goal. Research suggested that this would likely involve something like a siamese network, which can be an effective approach for solving problems such as facial recognition and signature verification. The key benefit of a siamese network is that it can perform verification tasks on input such as a pair of images. Verification is similar to classification, but instead of having many classes, e.g. one for each id, it has two, same and different. The idea for our project would be to pair an image of a person decomposed and with of them not decomposed to establish identity. Albeit a siamese network may not be perfect for this task, but it would be an interesting pursuit.
[pyimagesearch.com](https://pyimagesearch.com/2020/11/23/building-image-pairs-for-siamese-networks-with-python/)

## Reflection

Working on this project provided our team with valuable experience in applying machine learning to a real-world problem with forensic relevance. Throughout the
project, we adapted to changing tools, shifting machine learning models, learning to build and use a docker container, and build a UI in python. This project
challenged us to collaborate effectively, adjust roles as needed, and balance research with implementation. Most importantly, it sparked deeper interest in AI’s
potential in forensic science — particularly in advancing toward future features like identity verification using models such as Siamese networks.
