from copulas.multivariate import GaussianMultivariate
from copulas.datasets import sample_trivariate_xyz
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Generate some example data
data = sample_trivariate_xyz()
data.head()

copula = GaussianMultivariate()
copula.fit(data)

synthetic_data = copula.sample(len(data))
print("\n Now let ye")

def scatter_3d(data):
    """Plot 3 dimensional data in a scatter plot."""
    fig = plt.figure()
    position = 111

    ax = fig.add_subplot(position, projection='3d')
    ax.scatter(*(
        data[column]
        for column in data.columns
    ))
    ax.set_title("Copulads")
    ax.title.set_position([.5, 1.05])
    print("Mup")

    return ax

scatter_3d(synthetic_data)