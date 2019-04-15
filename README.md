# intelligent-toolkit-prognostic

Recently,  a  large  number  of  researchers  have  been employing  machine  learning  algorithms  to  sensor  data  for  pre-dicting aircraft part’s remaining useful life (RUL) with promising results.   An   in-depth   review   of   the   literature,   however,   hasrevealed  a  lack  of  consensus  regarding  (a)  evaluation  metrics adopted;  (b)  the  state-of-the-art  methods  employed  for  perfor-mance comparison; (c)  approaches  to  address  data  overfitting;and (d) statistical tests to assess results’ significance. The existing weaknesses in methodological approaches to experimental design,results evaluation, comparison and reporting of findings can re-sult in misleading outcomes and ultimately produce less effective predictors.  Arbitrary  choices  of  approaches  for  novel  method’sevaluation,  the  potential  bias  that  can  be  introduced,  and  the lack   of   systematic   replication   and   statistical   comparison   ofoutcomes might affect the findings reported and misguide future research.  For  further  advances  in  this  area,  there  is  thereforean urgent need for appropriate benchmarking methodologies to assist evaluating novel methods and to produce fair performance rankings.  In  this  paper  we  introduce  an  open-source,  extensible benchmarking library that will adress this gap in RUL research.The  objectives  are  to  assist  researchers  to  conduct  a  proper,fair  evaluation  of  their  novel  machine  learning  RUL  predictive models. In addition, we intend to stimulate better practices anda  more  rigorous  experimental  design  approach  across  the  field.

# Supplementary Results

## FD002
| Algorithms  | RE | ME | MAD | AE     | MdAE | Timeliness | MAE | RMSE | R^2 | sMAPE (%) | Training Time (s) | Testing Time (s) |
|-------------|----|----|-----|--------|------|------------|-----|------|-----|-----------|-------------------|------------------|
| SGD         |    |    |     | 11199.7|      | 63165.7    |     | 51.7 |     |           |                   |                  |
| Extra Trees |    |    |     |    |      | 18998.1    |     | 27.4 |     |           |                   |                  |
| AdaBoost    |    |    |     |    |      | 65739.4    |     | 37.4 |     |           |                   |                  |
| Bagging     |    |    |     |    |      | 158864.3   |     | 36.6 |     |           |                   |                  |
| RF          |    |    |     |    |      | 29751.2    |     | 27.9 |     |           |                   |                  |
| SVR         |    |    |     |    |      | 17898.6    |     | 30.3 |     |           |                   |                  |
| GBR         |    |    |     |    |      | 22943.8    |     | 28.2 |     |           |                   |                  |
| KNN         |    |    |     |    |      | 31063.8    |     | 28.5 |     |           |                   |                  |
| MLP         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| GRU         |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN2D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| CNN1D       |    |    |     |    |      |            |     |      |     |           |                   |                  |
| LSTM        |    |    |     |    |      |            |     |      |     |           |                   |                  |

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
