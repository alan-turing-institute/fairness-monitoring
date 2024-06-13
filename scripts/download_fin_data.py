# %% [markdown]
# # Download the finance-related text datasets
# %%
from IPython import get_ipython
from IPython.core.display import display, HTML
import pandas as pd
from io import StringIO
import datasets
from datasets import load_dataset
from tqdm.notebook import tqdm
from pathlib import Path

# %%
get_ipython().system('mkdir ../data')
datasets.config.DOWNLOADED_DATASETS_PATH = Path('../data')

# %%
# # Financial Reports SEC
# Homepage: <https://huggingface.co/datasets/JanosAudran/financial-reports-sec>

print ("Financial Reports SEC: Downloading the large_full")
dataset = load_dataset("JanosAudran/financial-reports-sec", "large_full")

# %%
# # Financial-PhraseBank 
# Homepage: <https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10>

print("Financial PhraseBank: Downloading the sentences_50agree")
fin_sentiment = load_dataset("financial_phrasebank", "sentences_50agree")

# %%
# AStock
# Homepage: <https://github.com/JinanZou/Astock>

print("AStock: Downloading the train, test, val, df_all_year_srl, and ood")
get_ipython().system('mkdir ../data/astock')
get_ipython().system('wget -O ../data/astock/train.csv https://raw.githubusercontent.com/JinanZou/Astock/main/data/train.csv')
get_ipython().system('wget -O ../data/astock/test.csv https://raw.githubusercontent.com/JinanZou/Astock/main/data/test.csv')
get_ipython().system('wget -O ../data/astock/val.csv https://raw.githubusercontent.com/JinanZou/Astock/main/data/val.csv')
get_ipython().system('wget -O ../data/astock/df_all_year_srl.csv https://raw.githubusercontent.com/JinanZou/Astock/main/data/df_all_year_srl.csv')
get_ipython().system('wget -O ../data/astock/ood.csv https://raw.githubusercontent.com/JinanZou/Astock/main/data/ood.csv')

# %%
# Financial Q&A Dataset
# Homepage: [FinQA](https://github.com/czyssrs/FinQA)

print("FinQA: Downloading the train, dev, and test")
get_ipython().system('mkdir ../data/finqa')
get_ipython().system('wget -O ../data/finqa/train.json https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/train.json') # Approximately 15MB
get_ipython().system('wget -O ../data/finqa/dev.json https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/dev.json') # Approximately 2MB
get_ipython().system('wget -O ../data/finqa/test.json https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/test.json') # Approximately 2MB

# %%
# Flare FinQA
# Homepage: <https://github.com/The-FinAI/PIXIU>

print("Flare FinQA: Downloading the flare-finqa")
dataset = load_dataset("ChanceFocus/flare-finqa") #Approximate Size: 16MB

# %%
# # ConvFinQA Dataset
# Homepage: <https://github.com/czyssrs/ConvFinQA>

print("ConvFinQA: Downloading the data")
get_ipython().system('mkdir ../data/convfinqa')
get_ipython().system('wget -O ../data/convfinqa/data.zip https://github.com/czyssrs/ConvFinQA/raw/main/data.zip') #Approximate Size: 17MB
get_ipython().system('unzip ../data/convfinqa/data.zip -d data/convfinq')
get_ipython().system('rm ../data/convfinqa/data.zip')

# %% 
# FLARE ConvFinQA
# Homepage: <https://huggingface.co/datasets/ChanceFocus/flare-convfinqa>

print("Flare ConvFinQA: Downloading the flare-convfinqa")
dataset = load_dataset("ChanceFocus/flare-convfinqa") #Approximate Size: 12 MB

# %%
# IBM FinTabNet
# Homepage <https://developer.ibm.com/exchanges/data/all/fintabnet/>

print("IBM FinTabNet: Downloading the fintabnet")
get_ipython().system('wget -O ../data/fintabnet.tar.gz https://dax-cdn.cdn.appdomain.cloud/dax-fintabnet/1.0.0/fintabnet.tar.gz') #Approximate Size: 16GB


# %%
# IBM SynthTabNet

print("IBM SynthTabNet: Downloading the synthtabnet")
get_ipython().system('wget -O ../data/synthtabnet.tar.gz https://ds4sd-public-artifacts.s3.eu-de.cloud-object-storage.appdomain.cloud/datasets/synthtabnet_public/v2.0.0/fintabnet.zip') #Approximate Size: 10GB

# %% [markdown]
# FinTabNet OTSL
# Homepage: <https://huggingface.co/datasets/ds4sd/FinTabNet_OTSL>

print("FinTabNet OTSL: Downloading the test")
dataset = load_dataset("ds4sd/FinTabNet_OTSL", split="test") # Approximate size: 300MB
