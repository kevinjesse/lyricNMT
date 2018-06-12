# A Neural Machine Translation on Lyric Dataset from Maroon 5.
The goal is to successfully generate lyrics given an initial set of words.

Read the [paper](https://github.com/kevinjesse/lyricNMT/blob/master/Lin205_Final_Report.pdf "Paper")!

## System Requirements
The code is successfully tested on Ubuntu 16.04 with a NVIDIA GPU GTX 1080 Ti. In order to run the code with this GPU you need to have the following software and libraries:
1. Python 3.6
2. [CUDA 8.0](https://developer.nvidia.com/cuda-80-ga2-download-archive)
3. CUDNN 7.1.4
4. [Anaconda](https://anaconda.org/)
It is possible to train the model on a unix based system using the CPU, but is not recommended.

## Project Structure
__main.py:__ The main process file to run the neural machine translation model. In main.py, we executed a five-step pipeline: (1) Load the dataset. (2) Define the model and training details. (3) Print out the configuration of the model and the hyperparameter setting for training. (4) Train the Model (5) Evaluate the best model on the test dataset. 

__preprocess.py:__ The program file that defines a set of functions that has been applied to load the data and prepare the batches for neural network.

__NMT_Seq2Seq.py:__ The model file that defines the Sequence to Sequence Model and the beamsearch decoding process.

__train.py:__ This script defines how we apply backpropagration to optimize the network. 

__layers/:__ Under this directory, we have defined the encoder and decoder structure and attention mechanism.

__evaluation/:__ BLEU score computation python script from [Google Neural Machine Translation Tutorial](https://github.com/tensorflow/nmt).

## Train the model
```
 python main.py --data_path data/lyric/data/ --trained_model_path ./ --sr en --tg vi
```
