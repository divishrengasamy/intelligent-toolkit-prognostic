# intelligent-toolkit-prognostic

Recently,  a  large  number  of  researchers  have  been employing  machine  learning  algorithms  to  sensor  data  for  pre-dicting aircraft part’s remaining useful life (RUL) with promising results.   An   in-depth   review   of   the   literature,   however,   has revealed  a  lack  of  consensus  regarding  (a)  evaluation  metrics adopted;  (b)  the  state-of-the-art  methods  employed  for  performance comparison; (c)  approaches  to  address  data  overfitting; and (d) statistical tests to assess results’ significance. The existing weaknesses in methodological approaches to experimental design,results evaluation, comparison and reporting of findings can result in misleading outcomes and ultimately produce less effective predictors.  Arbitrary  choices  of  approaches  for  novel  method’sevaluation,  the  potential  bias  that  can  be  introduced,  and  the lack   of   systematic   replication   and   statistical   comparison   of outcomes might affect the findings reported and misguide future research.  For  further  advances  in  this  area,  there  is  therefore an urgent need for appropriate benchmarking methodologies to assist evaluating novel methods and to produce fair performance rankings.  We  introduce  an  open-source,  extensible benchmarking library that will adress this gap in RUL research. The  objectives  are  to  assist  researchers  to  conduct  a  proper, fair  evaluation  of  their  novel  machine  learning  RUL  predictive models. In addition, we intend to stimulate better practices anda  more  rigorous  experimental  design  approach  across  the  field.

# Evaluation Results

## FD001
| Algorithms  | RE    | ME  | MAD | AE     | MdAE | Timeliness | MAE | RMSE | R²   | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|-------|-----|-----|--------|------|------------|-----|------|------|-----------|-------------------|------------------|
| SGD         | 61.8  | 25.2|20.5 | 2520.2 |22.2  | 2477.9     | 25.2| 30.4 | 0.464| 40.6      |   0.02            |   0.009               |
| Extra Trees | 31.8  | 19.2|17.6 | 1924.4 |11.7  | 1540.4     | 19.3| 25.9 | 0.621| 25.1      |   13.3            |   0.678               |
| AdaBoost    | 41.9  | 21.7|19.0 | 2166.4 |16.6  | 2050.9     | 21.8| 28.4 | 0.530| 31.1      |   32.7            |   0.023               |
| Bagging     | 48.3  | 21.3|17.6 | 2214.2 |18.1  | 1433.5     | 21.7| 26.8 | 0.559| 34.5      |   1.2             |   0.030               | 
| RF          | 31.8  | 19.0|18.0 | 1918.4 |12.1  | 1672.5     | 18.9| 25.7 | 0.609| 24.7      |   37.0            |   0.413               |
| SVR         | 36.5  | 19.7|17.5 | 1970.6 |13.3  | 1877.6     | 19.7| 25.5 | 0.622| 29.4      |   20.0            |   0.678               |
| GBR         | 31.9  | 19.4|19.0 | 1944.8 |13.9  | 1912.7     | 19.4| 26.7 | 0.586| 26.0      |   9.2             |   0.011               |
| KNN         | 33.1  | 20.7|19.1 | 2073.1 |14.5  | 2030.9     | 20.7| 27.7 | 0.553| 26.5      |   0.2             |   0.080               |
| MLP         | 30.7  |  5.2|17.4 | 1762.3 |13.2  |  1221.4    | 14.7| 21.6 | 0.720| 31.2      |   1051            |   0.048               |
| GRU         | 17.3  |  8.2|13.3 | 1268.5 |8.5   |  999.5     | 11.8| 17.7 | 0.610| 27.7      |   2625            |   0.071               |
| CNN2D       | 23.9  |  7.5|15.2 | 1550.3 |8.6   |  957.3     | 14.2| 21.2 | 0.670| 19.8      |   1725            |   0.238               |
| CNN1D       | 23.9  |  7.8|17.1 | 1616.6 |9.9   |  890.2     | 11.4| 18.0 | 0.780| 22.6      |   262             |   0.231               |
| LSTM        | 32.6  | 21.9|19.9 | 2228.9 |15.2  |  1147.4    | 14.6| 22.2 | 0.340| 22.6      |   402             |   0.084               |

## FD002
| Algorithms  | RE    | ME  | MAD | AE     | MdAE | Timeliness | MAE | RMSE | R²   | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|-------|-----|-----|--------|------|------------|-----|------|------|-----------|-------------------|------------------|
| SGD         | 482.9 | 43.2|33.2 | 11199.7|39.4  | 63165.7    | 43.2| 51.7 | 0.07 | 59.6      |   0.258           |   0.010               |
| Extra Trees | 88.6  | 20.1|19.3 | 5206.9 |13.2  | 18998.1    | 20.1| 27.4 | 0.73 | 27.9      |   56.1            |   2.78                 |
| AdaBoost    | 256.7 | 30.8|28.1 | 7985.0 |26.6  | 65739.4    | 30.8| 37.4 | 0.51 | 48.5      |   58.6            |   0.037               |
| Bagging     | 275.5 | 30.9|28.2 | 8017.5 |29.4  | 158864.3   | 30.9| 36.6 | 0.53 | 50.4      |   4.42            |   0.082               |
| RF          | 84.7  | 20.1|19.7 | 5224.6 |14.1  | 29751.2    | 20.1| 27.9 | 0.73 | 27.6      |   126.6           |   2.26                 |
| SVR         | 163.4 | 24.5|24.0 | 6352.7 |20.9  | 17898.6    | 24.5| 30.3 | 0.68 | 45.8      |   139.5           |   0.269               |
| GBR         | 94.2  | 20.9|20.7 | 5419.7 |13.5  | 22943.8    | 20.9| 28.2 | 0.72 | 33.3      |   32.4            |   0.016               |
| KNN         | 98.4  | 21.1|20.6 | 5481.3 |15.5  | 31063.8    | 21.1| 28.5 | 0.71 | 30.1      |   0.004           |   0.621               |
| MLP         | 82.5  | -2.5|18.0 | 4610.5 |11.3  | 27030.6    | 18.2| 25.7 | 0.77 | 45.2      |  1616.9           |   0.283               |
| GRU         | 233.2 | 13.3|27.2 | 7224.2 |26.2  | 60764.9    | 31.0| 37.9 | 0.48 |  50.1     |   3948.4          |   1.13               |
| CNN2D       | 188.8 | 12.8|27.9 | 7563.1 |23.4  | 311192.5   | 29.8| 39.8 | 0.44 | 43.5      |   127498.3        |   0.657               |
| CNN1D       | 141.0 | 3.36|28.7 | 6686.3 |21.2  |  3397654   | 28.7| 41.3 | 0.38 | 44.9      |   507.7           |   0.685               |
| LSTM        | 65.8  | -4.8|16.3 | 4089.5 |9.7   | 19640.3    | 17.5| 25.3 | 0.76 | 31.7      |  9245.2           |  0.279                |

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
| MLP         |30.6|5.10| 17.3| 1762.2 |13.2  |  1.37E+03  | 17.6| 23.2 |0.69  | 38.7      |  522.4            |   0.338                    |
| GRU         |27.7|15.2| 14.9| 1738.1 |10.8  |  6.64E+03  | 18.1| 27.9 |0.53  | 23.2      | 6046.3            |   0.386                    |
| CNN2D       |27.0|9.20| 18.0| 1820.9 |9.9   |  3.28E+04  | 18.2| 28.2 |0.53  | 29.7      |  3245.2           |   0.076                    |
| CNN1D       |37.4|7.36| 22.7| 2190.0 |13.5  |  2.63E+07  | 22.8| 37.5 |0.15  | 32.4      | 584.9             |  0.436                     |
| LSTM        |18.9|4.21| 14.9| 1439.8 |9.3   |  1.76E+03  | 14.9| 22.5 |0.69  | 19.2      | 3618.3            |  0.452                     |

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
| MLP         |        |    |       |         |      |            |      |      |        |           |                   |                   |
| GRU         |        |    |       |         |      |            |      |      |        |           |                   |                   |
| CNN2D       |        |    |       |         |      |            |      |      |        |           |                   |                   |
| CNN1D       |        |    |       |         |      |            |      |      |        |           |                   |                   |
| LSTM        |        |    |       |         |      |            |      |      |        |           |                   |                   |
