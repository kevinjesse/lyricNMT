import os
import torch
from torch.autograd import Variable
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import math
from random import randint

def train_nmt(input_variable,target_variable,input_lengths,model,criterion,optimizer,teacher_force_ratio=0.5,clip=1.0):
    #specify this is the training stage
    model.train()
    #Zero gradients of the optimizer
    optimizer.zero_grad()
    #FeedForward
    loss= model(input_variable,input_lengths,target_variable,teacher_force_ratio,criterion=criterion)

    #Backpropagate the Loss
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(),clip)
    optimizer.step()

    return loss.item()

#Randomly Display Some Results
def random_sample_display(test_data,output_list):
    sample_index = randint(0,len(test_data)-1)
    sample_source = test_data[sample_index][0]
    sample_ref = test_data[sample_index][1]
    sample_output_tokens = output_list[sample_index]
    sample_output = ' '.join(sample_output_tokens)
    return sample_source, sample_ref, sample_output
