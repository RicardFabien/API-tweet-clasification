# API-tweet-clasification
## Introduction
This application is a simple docker app that uses Machine learning to tell you whether or not the sentenced you entered is offensive, hate speech or neither. <br>
![image](https://user-images.githubusercontent.com/49694912/145221021-9ec8e3a6-df66-432b-8022-435529bfd5c3.png) <br>
Just enter a sentence, click on the button and you'll get an answer

## Composition
The app in itself is the `main.py` file, which load up the machine learning model contained in `model.pkl`, and uses the folder `templates/` to store its (only) page <br>
The other files are used to load up the docker app or (re)generate the `model.pkl` file

## How to use
### How to launch the app
#### Recommended use
It is recommended that you launch the app in a docker and use a browser to access it. <br>
To do so, you need to have Docker installed. <br>
To do so, you have a list of commands provided below, to use in the folder of the project : 
```
Docker build -t t_class .
Docker run --name t_class -p 5000:5000 classifier
```
And if these command has already been used once without error :
```
Docker start classifier
```
You can use different names as the ones used here, if you want to do so please refer to this documentation: https://docs.docker.com/engine/reference/run/ .

#### Alternative use
You can directly launch `main.py` with python (not recommended as it needs you to have a terminal open and closing it would terminate the app) <br>
To do so, you need to have python installed, as well as the libaries : 
- flaks
- joblib
- pandas
- sklearn
(Those librairies can be installed with the command `pip install flask joblib pandas sklearn`, provided that you have pip installed and a stable internet connection, refer to https://pip.pypa.io/en/stable/installation/ for the instalation of pip)
In a terminal, in the same folder as main.py, write the command :
```
python main.py
```
### How to use the launched app
With a broswer, navigate to the adress localhost:5000, and you should get the main page of the app <br>

## Change the dataset used for the model
The model is already provided for the app, but it is possible to reload a new one, using `model_maker.py` and `label.csv` <br>
For that you need to have installed `python` and the libraries `joblib`, `pandas` and `sklearn`. <br> <br>
If you want to switch the database used by the model, you need to switch the `label.csv` provided with one of yours.
The file must be in the csv format and be in the format  : 

```
tweet,class
Un tweet,2
A fucking other tweet,1
A foul tweet,0
```

| tweet        | class           |
| ------------- |:-------------:|
| Un tweet      | 2 |
| A fucking other tweet      | 1      |
| A foul tweet | 0      |


With `tweet` being the tweet and `class` being the class of the tweet (0 for hate speech, 1 for offensive language and 2 for neither) <br>
You can add other column to the file, they won't be taken into account <br>
<br>
Once your file is ready, open a terminal in the same folder as `model_maker` and use the command `python model_maker.py` <br>
The operation might take some time
<br>
<br>
HTML encoding (such as turning `&` into `&amp`) will be reversed before processing
It is recommended that you get at the very list 50 instances to make sure that you get accurate predictions, although, considering the subject of the prediction, a number around 100 000/ 1M would be more useful


-  See [License](LICENSE)
