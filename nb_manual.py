"""Các hàm nhỏ giúp hiểu cơ chế Gaussian Naive Bayes.

Sinh viên chỉ hoàn thiện hai hàm dưới đây; không cần tự cài toàn bộ GaussianNB.
"""

import math


def compute_class_priors(y):
    """Trả về dict {class_label: prior_probability}."""
    # TODO: đếm số phần tử của từng lớp và chia cho tổng số mẫu.
    raise NotImplementedError("TODO: implement compute_class_priors")


def gaussian_log_likelihood(x, mean, var):
    """Tính log p(x | class) với giả định Gaussian một chiều.

    Công thức:
        -0.5 * log(2*pi*var) - (x-mean)^2 / (2*var)
    """
    # TODO: kiểm tra var > 0 và cài đặt công thức ở trên.
    raise NotImplementedError("TODO: implement gaussian_log_likelihood")
