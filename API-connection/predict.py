import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User


def predict_user(user_name):
    user = User.query.filter(User.name == user_name).one()
    user_vects = np.array([vect for vect in user.tweets])
    vects = np.vstack([user_vects])
    labels = np.concatenate(
        [np.zeros(len(user.User)])

    log_reg = LogisticRegression().fit(vects, labels)

    return log_reg.predict(_vect.reshape(1, -1))