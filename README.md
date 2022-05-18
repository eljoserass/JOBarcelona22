
# JOBarcelona2022 Submission

Link to the description of the challenge: https://nuwe.io/challenge/jobarcelona-22-data

Implementaion of a KNearest Neighbors algorithm for solving the proposed clasification problem.

You will find the results of the predictions for the input dataset './datasets/test_x.csv' 
in './results.csv'.

This predictions where made based on './datasets/train.csv'


## Installation

It uses some python dependencies. These are the commands to install them in a debian based linux distribution

```bash
  pip install scikit-learn
  pip install numpy
  sudo apt install python3-pandas
```
    
## Usage/Examples

```bash
USAGE
        ./program --train <path_to_train_dataset.csv> --test <path_to_test_dataset.csv>
DESCRIPTION
        Use --train and --test to train and test model on custom dataset
        If no argument is provided, the program will run with the defaults .csv in the /datasets folder
        The results will be written in a .csv file called results.csv
```

It is expected that de datasets are in the correct path and follow the next structures:      

For training:
```csv
,Hour,Minutes,Sensor_alpha,Sensor_beta,Sensor_gamma,Sensor_alpha_plus,Sensor_beta_plus,Sensor_gamma_plus,Insect
0,22,26,119.91099509914545,242.83832442154588,-316.8192224546028,250.19504806941768,-53.54777743704835,-112.04998339216505,2
1,10,16,-90.79053622505052,-269.47076686616987,-182.58184393846824,95.39494140607357,37.291944096151106,48.52518002541007,0
2,21,42,-20.02800301547547,-147.07021163438992,50.280871737663226,-90.7503861661937,-50.47655566005774,85.39900868624007,1
...
```

For testing;
```csv
,Hour,Minutes,Sensor_alpha,Sensor_beta,Sensor_gamma,Sensor_alpha_plus,Sensor_beta_plus,Sensor_gamma_plus
7000,21,31,-72.08358487232044,-11.434977441229432,-52.9617428108554,-72.69638489124168,145.29922715050168,-143.85624268199984
7001,21,3,-193.6199802062626,40.13708050140161,85.41924440271838,-26.266801499519328,-125.39123723502519,80.90497332151413
7002,22,31,42.578382115156124,-51.6134016768775,125.05561141969137,182.136745856363,-9.72695105917094,-114.91340177688434
...
```

Results:

```csv
Test_index,Insect
7000,1
7001,0
7002,0
...
```
## Author

- [@eljoserass](https://www.github.com/eljoserass)

