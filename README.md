The aim is to build a tool that can take a scanning of a piece of paper with diagrams, tables, handwritten notes, regular computer-printed text, images, and other information and turn it into digital data that is reformattable and useful.


The plan is to use existing models to perform OCR on computer-printed and handwritten text and train a new segmentation-based model to extract semantic meaning from the relative positions of visual elements of information. These elements could include text paragraphs, charts, graphs, arrows, curly braces, tables, images, icons, and more. 


Motivation:
I had trouble syncing my digital notes on my iPad with my laptop and being able to do meaningful things with that data. However, no such tools exist to "just know" what the placement of different pieces of text and non-text mean. Hopefully, this project can grow into something that moves the needle forward in OCR and AI.

I'm using FastAPI for the backend since FastAPI has high performance and is easy to develop a back-end with due to its simplicity, which allows a beginner like me to create an app faster. This app will also allow the quick processing of photos taken from a phone for AI/OCR. For the AI, I will be using PyTorch as this AI/ML library has a vast community and contains many functions, features, and tools to create AI models with flexibility.
