import re;
import csv;
import time;
import httpagentparser as http;


class modifiedNB():
    
    def __init__(self,filename,resp_var,static_var,dynamic_var = None,file_sep = "\t",
                 equal_prior = True,train_prop = 0.5,split = True,markov_order = 1 ):
        self.filename = filename;
        self.resp_var = resp_var;
        self.static_var = static_var;
        self.dynamic_var = dynamic_var;
        self.file_sep = "\t";
        self.equal_prior = equal_prior;        
        pass;
    