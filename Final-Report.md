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

  * Hugging Face Libraries

The Hugging Face Transformers library was used in this project to find and fine-tune models and facilitate image classification. Hugging Face is platform for sharing and finding machine learning models and data sets. They have open source software for interacting with their online repositories and using models and data sets. The code for this project was directly inspired from the image classification example in the Hugging Face Transformers repository. The library provides a user friendly way to load and split data, download models, fine-tune models, and run tasks such as image classification with those models. The most critical part of the library for the purposes of this project is the Trainer class which takes in the model, the data set, the image processor, and the collate function and other configurations. This class automates the fine-tuning which this project uses with the body farm data to classify images.
[huggingface.co](https://huggingface.co/)

### Changes:

### Testing and Results:
    

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
