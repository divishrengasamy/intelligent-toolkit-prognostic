# intelligent-toolkit-prognostic

Recently,  a  large  number  of  researchers  have  been employing  machine  learning  algorithms  to  sensor  data  for  pre-dicting aircraft part’s remaining useful life (RUL) with promising results.   An   in-depth   review   of   the   literature,   however,   hasrevealed  a  lack  of  consensus  regarding  (a)  evaluation  metrics adopted;  (b)  the  state-of-the-art  methods  employed  for  perfor-mance comparison; (c)  approaches  to  address  data  overfitting;and (d) statistical tests to assess results’ significance. The existing weaknesses in methodological approaches to experimental design,results evaluation, comparison and reporting of findings can re-sult in misleading outcomes and ultimately produce less effective predictors.  Arbitrary  choices  of  approaches  for  novel  method’sevaluation,  the  potential  bias  that  can  be  introduced,  and  the lack   of   systematic   replication   and   statistical   comparison   ofoutcomes might affect the findings reported and misguide future research.  For  further  advances  in  this  area,  there  is  thereforean urgent need for appropriate benchmarking methodologies to assist evaluating novel methods and to produce fair performance rankings.  In  this  paper  we  introduce  an  open-source,  extensible benchmarking library that will adress this gap in RUL research.The  objectives  are  to  assist  researchers  to  conduct  a  proper,fair  evaluation  of  their  novel  machine  learning  RUL  predictive models. In addition, we intend to stimulate better practices anda  more  rigorous  experimental  design  approach  across  the  field.

# Supplementary Results

## FD002
| Algorithms  | RE    | ME  | MAD | AE     | MdAE | Timeliness | MAE | RMSE | R^2  | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|-------|-----|-----|--------|------|------------|-----|------|------|-----------|-------------------|------------------|
| SGD         | 482.9 | 43.2|33.2 | 11199.7|39.4  | 63165.7    | 43.2| 51.7 | 0.073| 59.6      |   0.064           |                  |
| Extra Trees | 88.6  | 20.1|19.3 | 5206.9 |13.2  | 18998.1    | 20.1| 27.4 | 0.738| 27.9      |   58.6            |                  |
| AdaBoost    | 256.7 | 30.8|28.1 | 7985.0 |26.6  | 65739.4    | 30.8| 37.4 | 0.514| 48.5      |   51.5            |                  |
| Bagging     | 275.5 | 30.9|28.2 | 8017.5 |29.4  | 158864.3   | 30.9| 36.6 | 0.534| 50.4      |   3.97            |                  |
| RF          | 84.7  | 20.1|19.7 | 5224.6 |14.1  | 29751.2    | 20.1| 27.9 | 0.730| 27.6      |   110.5           |                  |
| SVR         | 163.4 | 24.5|24.0 | 6352.7 |20.9  | 17898.6    | 24.5| 30.3 | 0.682| 45.8      |   141.9           |                  |
| GBR         | 94.2  | 20.9|20.7 | 5419.7 |13.5  | 22943.8    | 20.9| 28.2 | 0.723| 33.3      |   29.9            |                  |
| KNN         | 98.4  | 21.1|20.6 | 5481.3 |15.5  | 31063.8    | 21.1| 28.5 | 0.717| 30.1      |   0.011           |                  |
| MLP         |    |    |     |        |      |            |     |      |     |           |                   |                  |
| GRU         |    |    |     |        |      |            |     |      |     |           |                   |                  |
| CNN2D       |    |    |     |        |      |            |     |      |     |           |                   |                  |
| CNN1D       |    |    |     |        |      |            |     |      |     |           |                   |                  |
| LSTM        |    |    |     |        |      |            |     |      |     |           |                   |                  |

## FD003
| Algorithms  | RE | ME | MAD | AE | MdAE | Timeliness | MAE | RMSE | R^2 | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|----|----|-----|----|------|------------|-----|------|-----|-----------|-------------------|------------------|
| SGD         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| Extra Trees |    |    |     |    |      |            |     |      |     |           |                   |                  |
| AdaBoost    |    |    |     |    |      |            |     |      |     |           |                   |                  |
| Bagging     |    |    |     |    |      |            |     |      |     |           |                   |                  |
| RF          |    |    |     |    |      |            |     |      |     |           |                   |                  |
| SVR         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| GBR         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| KNN         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| MLP         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| GRU         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN2D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN1D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| LSTM        |    |    |     |    |      |            |     |      |     |           |                   |                  |

## FD004
| Algorithms  | RE | ME | MAD | AE | MdAE | Timeliness | MAE | RMSE | R^2 | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|----|----|-----|----|------|------------|-----|------|-----|-----------|-------------------|------------------|
| SGD         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| Extra Trees |    |    |     |    |      |            |     |      |     |           |                   |                  |
| AdaBoost    |    |    |     |    |      |            |     |      |     |           |                   |                  |
| Bagging     |    |    |     |    |      |            |     |      |     |           |                   |                  |
| RF          |    |    |     |    |      |            |     |      |     |           |                   |                  |
| SVR         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| GBR         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| KNN         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| MLP         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| GRU         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN2D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN1D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| LSTM        |    |    |     |    |      |            |     |      |     |           |                   |                  |
