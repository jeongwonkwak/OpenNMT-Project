# OpenNMT based Korean-to-English Neural Machine Translation (NMT)
This repo contains the source code and other details for a neural machine translation based on attention using pytorch. This model translates Korean into English.   

## Capstone Project (2020.02 ~ )
* **Weekly Report** : [check here](https://github.com/SoYoungCho/Korean-English-NMT/wiki/Weekly-Report-%231) :)  
From February 2020, the weekly report can be found there.

## Performance

* **BLEU(Bilingual Evaluation Understudy) score** 

| BLEU | BLEU1 | BLEU2 | BLEU3 | BLEU4 | 
|---|:---:|:---:|:---:|:---:|
| **33.55** | 64.6 | 40.0 | 27.5 | 19.4 | 

* **Translation Sentence**  

Example 1 
```
차를 마시러 공원에 가던 차 안에서 나는 그녀에게 차였다.
```
```
> I was dumped by her in a car on the way to the park to drink tea .  
```
Example 2  
```
사과의 의미로 사과를 먹으며 사과했다.
```
```
> I apologize while eating an apple for the meaning of an apology .
```
Example 3
```
내가 그린 기린 그림은 긴 기린 그림이냐, 그냥 그린 기린 그림이냐?
```
```
> Is the giraffe I drew a long giraffe picture or just a giraffe picture ?
```
---
## How to use

### Step 1. Preprocess the data
```
!python preprocess.py
```

### Step 2. Train the model
```
!python train.py
```
If you want to continue training the model, add `--train_from (model_path)/model.pt` later.

### Step 3. Translate
```
!python translate.py -model data/model/model.pt -src data/src-test.txt -tgt data/tgt-test.txt -replace_unk -verbose -gpu 0
```

### Step 4. Scoring the model
```
!perl tools/multi-bleu.perl data/tgt-test.txt < pred.txt
```

### step 5. Excute GUI
```
!pyhton gui.py
```

## Reference
https://github.com/OpenNMT/OpenNMT-py
