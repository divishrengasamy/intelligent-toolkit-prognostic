# intelligent-toolkit-prognostic

Recently,  a  large  number  of  researchers  have  been employing  machine  learning  algorithms  to  sensor  data  for  pre-dicting aircraft part’s remaining useful life (RUL) with promising results.   An   in-depth   review   of   the   literature,   however,   has revealed  a  lack  of  consensus  regarding  (a)  evaluation  metrics adopted;  (b)  the  state-of-the-art  methods  employed  for  performance comparison; (c)  approaches  to  address  data  overfitting; and (d) statistical tests to assess results’ significance. The existing weaknesses in methodological approaches to experimental design,results evaluation, comparison and reporting of findings can result in misleading outcomes and ultimately produce less effective predictors.  Arbitrary  choices  of  approaches  for  novel  method’sevaluation,  the  potential  bias  that  can  be  introduced,  and  the lack   of   systematic   replication   and   statistical   comparison   of outcomes might affect the findings reported and misguide future research.  For  further  advances  in  this  area,  there  is  therefore an urgent need for appropriate benchmarking methodologies to assist evaluating novel methods and to produce fair performance rankings.  We  introduce  an  open-source,  extensible benchmarking library that will adress this gap in RUL research. The  objectives  are  to  assist  researchers  to  conduct  a  proper, fair  evaluation  of  their  novel  machine  learning  RUL  predictive models. In addition, we intend to stimulate better practices anda  more  rigorous  experimental  design  approach  across  the  field.

# Supplementary Results

## FD002
| Algorithms  | RE    | ME  | MAD | AE     | MdAE | Timeliness | MAE | RMSE | R²   | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|-------|-----|-----|--------|------|------------|-----|------|------|-----------|-------------------|------------------|
| SGD         | 482.9 | 43.2|33.2 | 11199.7|39.4  | 63165.7    | 43.2| 51.7 | 0.073| 59.6      |   0.064           |                  |
| Extra Trees | 88.6  | 20.1|19.3 | 5206.9 |13.2  | 18998.1    | 20.1| 27.4 | 0.738| 27.9      |   58.6            |                  |
| AdaBoost    | 256.7 | 30.8|28.1 | 7985.0 |26.6  | 65739.4    | 30.8| 37.4 | 0.514| 48.5      |   51.5            |                  |
| Bagging     | 275.5 | 30.9|28.2 | 8017.5 |29.4  | 158864.3   | 30.9| 36.6 | 0.534| 50.4      |   3.97            |                  |
| RF          | 84.7  | 20.1|19.7 | 5224.6 |14.1  | 29751.2    | 20.1| 27.9 | 0.730| 27.6      |   110.5           |                  |
| SVR         | 163.4 | 24.5|24.0 | 6352.7 |20.9  | 17898.6    | 24.5| 30.3 | 0.682| 45.8      |   141.9           |                  |
| GBR         | 94.2  | 20.9|20.7 | 5419.7 |13.5  | 22943.8    | 20.9| 28.2 | 0.723| 33.3      |   29.9            |                  |
| KNN         | 98.4  | 21.1|20.6 | 5481.3 |15.5  | 31063.8    | 21.1| 28.5 | 0.717| 30.1      |   0.011           |                  |
| MLP         |       |     |     |        |      |            |     |      |     |            |                   |                  |
| GRU         |       |     |     |        |      |            |     |      |     |            |                   |                  |
| CNN2D       |       |     |     |        |      |            |     |      |     |            |                   |                  |
| CNN1D       |       |     |     |        |      |            |     |      |     |            |                   |                  |
| LSTM        |       |     |     |        |      |            |     |      |     |            |                   |                  |

## FD003
| Algorithms  | RE | ME | MAD | AE     | MdAE | Timeliness | MAE | RMSE | R²   | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|----|----|-----|--------|------|------------|-----|------|------|-----------|-------------------|------------------|
| SGD         |91.7|37.8| 30.9| 3780.7 |35.9  | 2.9569e+04 |37.8 | 45.2 |-0.195| 55.6      |  0.137            |   0.002               |
| Extra Trees |41.2|29.4| 25.5| 2945.2 |16.3  | 6.1131e+04 | 29.4| 41.8 |-0.020| 31.3      |  6.763            |   0.044               |
| AdaBoost    |62.3|37.9| 29.0| 3796.3 |29.6  | 1.7930e+05 | 37.9| 50.2 |-0.474| 43.4      |  119.9            |   0.065               |
| Bagging     |83.2|40.0| 23.5| 4007.1 |33.4  | 6.3764e+04 | 40.0| 48.5 |-0.376| 49.4      |  0.494            |   0.013               |
| RF          |38.9|27.6| 24.4| 2762.6 |17.4  | 2.1875e+04 | 27.6| 38.9 |0.114 | 30.2      |  25.9             |   0.041               |
| SVR         |45.3|30.9| 28.0| 3093.0 |19.8  | 1.1169e+07 | 30.9| 45.4 |-0.206| 34.6      |   28.0            |   0.099               |
| GBR         |38.3|26.6| 24.1| 2668.6 |16.6  | 1.0130e+04 | 26.6| 37.2 |0.189 | 31.8      |   10.2            |   0.004               |
| KNN         |42.4|31.0| 27.8| 3105.9 |19.4  | 3.4243e+06 | 31.0| 45.5 |-0.210| 31.8      |   0.023           |   0.071               |
| MLP         |    |    |     |        |      |            |     |      |      |           |                   |                       |
| GRU         |    |    |     |        |      |            |     |      |      |           |                   |                       |
| CNN2D       |    |    |     |        |      |            |     |      |      |           |                   |                       |
| CNN1D       |    |    |     |        |      |            |     |      |      |           |                   |                       |
| LSTM        |    |    |     |        |      |            |     |      |      |           |                   |                       |

## FD004
| Algorithms  | RE    | ME   | MAD  | AE      | MdAE | Timeliness | MAE  | RMSE | R²     | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|-------|------|------|---------|------|------------|------|------|--------|-----------|-------------------|------------------|
| SGD         | 421.4 | 48.1 | 45.7 | 11935.7 | 41.0 | 8.6462e+08 | 48.1 | 59.8 | -0.204 | 68.7      |  0.126            |        0.011      |
| Extra Trees | 108.1 | 27.6 | 24.2 | 6852.2  | 19.4 | 5.0815e+04 | 27.6 | 37.5 | 0.525  | 33.0      |   51.5            |        2.5        |
| AdaBoost    | 256.3 | 41.3 | 31.2 | 10259.5 | 39.3 | 1.0710e+05 | 41.3 | 49.6 | 0.169  | 52.3      |   139.3           |        0.058      |
| Bagging     | 357.8 | 42.3 | 33.2 | 10511.4 | 38.2 | 8.7822e+04 | 42.3 | 51.1 | 0.120  | 54.8      |    2.5            |        0.044      |
| RF          | 102.7 | 27.9 | 25.4 | 6930.3  | 19.0 | 8.0127e+04 | 27.9 | 38.6 | 0.496  | 32.3      |    170.1          |        2.7        |
| SVR         | 136.9 | 29.3 | 27.1 | 7278.3  | 24.8 | 3.4864e+04 | 29.3 | 37.2 | 0.532  | 42.8      |    144.9          |        0.351      |
| GBR         | 116.5 | 29.2 | 26.1 | 7261.7  | 21.3 | 2.5839e+05 | 29.2 | 40.3 | 0.451  | 37.4      |    31.3           |        0.025      |
| KNN         | 123.3 | 30.0 | 27.1 | 7455.7  | 22.2 | 9.0328e+04 | 30.0 | 40.2 | 0.453  | 36.1      |    0.114          |        0.230      |
| MLP         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| GRU         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN2D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN1D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| LSTM        |    |    |     |    |      |            |     |      |     |           |                   |                  |
