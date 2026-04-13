import torch.nn as nn 





# vanilla RNN class
class RNN(nn.Module):
    #constructor method to initialize the RNN
    def _init_(self,input_size,hidden_size,output_size):
        super(RNN,self)._init_()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.h2o = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)
    #forward method to define the forward pass of the RNN
    def forward(self,input,hidden):
        combined = torch.cat((input,hidden),1)
        hidden = self.i2h(combined)
        output = self.h2o(hidden)
        output = self.softmax(output)

        #return output and and new hidden state 
        return output, hidden
    #method to initialize the hidden state of the RNN
    def initHidden(self):
        return torch.zeros(1,self.hidden_size)
    
# hidden layer size to 128 neurons
n_hidden = 128

#create an instance of the RNN with: 
rnn = RNN(n_letters, n_hidden, n_categories)
