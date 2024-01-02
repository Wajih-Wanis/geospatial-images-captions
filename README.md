This project's goal is to : Design and implement an an end-to-end application proptotype that takes multispectral geospatial ‎images 
as input, uses DL for image recognition, and LLM for generating descriptive ‎captions for those 
images.
For this project I have used the gpt-2-captionning which is a llm pretrained to caption images with the help of other transformers which job is to extract visual data, for the moment it only works on RGB pictures thus the image_process class which transforms the spectral images from satellites into RGB images to describe its content. 
This project could be further improved with finetuning for specific image datasets and adding the ability to directly describe satellite spectral images.
After that the model is served as an api using flask.