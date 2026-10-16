# algorithm/

The core logic of your value-adding algorithm: feature engineering, scoring, ranking,
training and prediction. It has to be in this repository, written by your group.

Keep it as plain Python functions that take data and return a result, without Flask
and without the database. A route fetches the data, calls your function, and passes
the result to a template. That way you can test the algorithm on its own, with a few
rows you make up, and explain it at the defence without a running application.

```python
# algorithm/recommend.py
def recommend(viewed, listings, n=5):
    ...

# routes/listings.py
from algorithm.recommend import recommend
```

Standard libraries such as scikit-learn, NumPy or pandas are fine. Add them to
requirements.txt the moment you install them.
