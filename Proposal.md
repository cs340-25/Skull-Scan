# Skull-Scan

## Heading
TBD

## Introduction

### The Project:
The Skull-Scan software will use a database of images and associated data to train a machine-learning model. The software will use the model to make predictions about expected data relationships when given some images as input.

### Background:
Our team is composed of talented, young individuals, motivated to learn about the power and beauty of machine learning. Our motivation for this project is manifold: to gain knowledge, skill, experience with machine learning, especially in relation to image processing, and to produce a functioning image analysis tool that can assist users in making predictions or estimations based on an individual image.

### Details & Vision:
Our project can be broken up into several steps. We already have a dataset to work with, but we need to parse out the data that will be useful for our purposes. We will also need to pull that data from the database and format it to work efficiently for training the model. This may include cropping images to exclude extraneous information. We will likely need more data from outside our current dataset, so we may need to write software to find and collect images and data or databases from the internet. Once we get all the data we need to work with, we will start training our data model. We will use the data model to make multiple data predictions with reasonable accuracy. This software should be modular enough to function with different datasets and varying goals for the data. It should be reusable and intuitive to work with.

### Motivation:
Specifically, we are interested in using this software to make estimations about deceased individuals, such as age at death, sex, stage of decomposition, what their faces might have looked like before death, and potentially to match an image of a skull to that of an undecomposed face. We will attempt to do this based on an image of their head at an advanced stage of decomposition.

An alternative example of how this software might be used could be analyzing an image of an analog clock and audibly announcing the time indicated by the clock, or determining how many clocks are in a photo and what times they indicate. 


## Customer Value

### Customer Need:
Our software will provide tremendous customer value. Our forensic customers need to identify bodies and close investigations. With this software, they will be able to make educated guesses about the identity of a victim of murder. Our anthropologist customers need our software to research ancient civilizations and uncover the secrets of our past. The blind need to know what time a clock says.

### Proposed Solution:
Our solution will deliver accurate, state-of-the-art predictions and estimations based on patterns and data. It will give our customers what they need most when they need it most.

### Measures of Success:
The success of our endeavor will be measured by the accuracy and breadth of our predictions. As well as the modularity and multipurpose potential of our software.


## Proposed Solution & Technology
### System:
  * Our software will use AI to help process the data faster
  * The main system would be comprised of the LLM for image processing, the database for storage and quick retrieval, and the framework to ensure all components work together
  * The minimal system would have to be able to get images and basic information from the image
  * We will test the system incrementally building it in parts that can be useful, even if not fully complete
    
### Tools: 
  * We plan on building our project using Python for as much as possible
  * We will also be using an LLM such as Llama or similar to assist in the lookup and retrieval of information
    

## Team
### Skills:
  * Has anyone on the team built something like this before? 
  * Are the tools known or new to the team?
    
### Roles:
  * What are the roles of the team members? 
  * Will the roles be fixed or rotating? 


## Project Management
### Schedule
We see completion as being possible, depending on how much we decide to implement. 
Our goal will be to meet at least once a week to ensure we are completing tasks, and looking at upcoming features to add or tasks to move higher in our priority.
Our general schedule outline is as follows, but is likely to change to meet the course requirements: 
   * Weeks: 1-2 (build a database, decide on LLM)
   * 3-4 (test out image recognition on database) 
   * 5-10 (implement weeks 1-4 work together) 
   * 11-13 (make final changes and make final presentable)

### Constraints/Resources
We have been given access to images provided by the bodyfarm on campus, to fill our database with. We just have to ensure that the images are of high enough quality 
to be processed. 

These images may be owned by the University, so we may not have the ability to share any outside our group.

### Descoping 
We are not worried about the full functionality of our software, as we will be implementing stages of it together.
This ensures that we have a working stage before we move on to the next phase of the project. 

This software has many uses, far beyond what we are planning on creating this semester. 
It has uses in all cases of Law Enforcement, Forensics, or everyday life for the average person.
