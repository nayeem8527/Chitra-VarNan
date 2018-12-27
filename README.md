# Chitra-VarNan

The ability to recognize image features for generating textual description is very important for many tasks in computer vision. Here, in this project we are tackling this problem for Hindi language and hence generating captions in Hindi.

# Approach

MSCOCO 2014 dataset is used for training and testing and their english image captions are being translated into Hindi captions using google translate api. Here, we have assumed that the translation done by google translate are correct and can be used as ground truth for training the sequence to sequence framework of tensorflow. Pre-trained VGG network is used for extracting the features from images which is further passed to LSTM for training to generate hindi captions. For evaluation we have used the BLUE metrics i.e Bilingual Evaluation Understudy Score which is an algorithm for evaluating the quality of text which has been machine-translated from one natural language to another(1 means perfect match and 0 means bad match of two texts) .

# Results

![screenshot from 2018-12-23 17-11-24](https://user-images.githubusercontent.com/10145585/50383260-fafa0200-06d5-11e9-9398-3bb8ec7a3233.png)

# Running the Code

**Preparing the data**
The framework will take tfrecord file as input. For making it run:
  
    python tfreader.py

After updating the required field in the file.

**Training the model**

    python /im2txt/train.py --input_file_pattern="TFRECORD FILE PATH" --inception_checkpoint_file="inception_v3.ckpt"   --train_dir="PATH TO STORE THE MODEL" --train_inception=false --number_of_steps=1000000
    
**Testing the model**

    python /im2txt/run_inference.py --checkpoint_path="TRAINED MODEL" --vocab_file="word_counts.txt" --input_files="IMAGE FILE"

# References

1. Karpathy, Andrej, and Li Fei-Fei. "Deep visual-semantic alignments for generating image descriptions." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015.
2. Lin, Tsung-Yi, et al. "Microsoft coco: Common objects in context." European conference on computer vision. Springer, Cham, 2014.
3. https://en.wikipedia.org/wiki/BLEU 
