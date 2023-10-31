This is a github repository that modifies the code in “Are Transformers Effective for Time Series Forecasting?” and applies it to other datasets.

The source of the existing code can be found at the link below.

# Are Transformers Effective for Time Series Forecasting? (AAAI 2023)

This repo is the official Pytorch implementation of LTSF-Linear: "[Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/pdf/2205.13504.pdf)". 

# The changed source files and contents are below.

run_longExp.py

It was used to modify the default value of the passed argument.

exp_main.py

Modified and added output result files and metrics.

data_loader.py

There was data preprocessing and border adjustment.

cow.sh

This is a newly created sh file for execution.


## Citing

If you find this repository useful for your work, please consider citing it as follows:

```bibtex
@inproceedings{Zeng2022AreTE,
  title={Are Transformers Effective for Time Series Forecasting?},
  author={Ailing Zeng and Muxi Chen and Lei Zhang and Qiang Xu},
  journal={Proceedings of the AAAI Conference on Artificial Intelligence},
  year={2023}
}
```

Please remember to cite all the datasets and compared methods if you use them in your experiments.
