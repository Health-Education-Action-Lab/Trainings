#########################################################################################
#   This training will showcase exploratory data analysis methods in Python using our
#   HEAL lab projects as a context.
#     Coded by Jeff Swigert
#     Last Updated: 1/17/2020
#     Based on material covered in EDA in Python datacamp.com course
#########################################################################################

#### Need to load all the packages we'll need ####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### Let's load the Talkspace Aggregate
data = pd.read_csv("")
data.head()


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y


# Compute ECDFs for the om_score_ids they give us.
x_1, y_1 = ecdf(
)  # TODO: need to reference column of the aggregate data for each variable
x_2, y_2 = ecdf()
x_3, y_3 = ecdf()

# Plot all ECDFs on the same plot
plt.plot(x_1, y_1, marker='.', linestyle='none')
plt.plot(x_2, y_2, marker='.', linestyle='none')
plt.plot(x_3, y_3, marker='.', linestyle='none')

# Annotate the plot
plt.legend(('1', '2', '3'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
