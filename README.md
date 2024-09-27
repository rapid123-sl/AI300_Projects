# AI300_Projects

## Codebase Author(s)

```
Samuel

```

## Folder Structure

```
├── model
│   └── capstone_catboost_model.pkl
├── notebooks
│   └── research_AI300_SamuelLee.ipynb
├── src
│   └── static
│      └── styling.css
│   └── templates
│      └── home.html
│   └── app.py
│   └── input_processing.py
│   └── model.py
├── .gitignore
├── README.md
├── requirements.txt

```

## Website URL of deployed Flask web application 

```
[Deployed Web App URL](http://ec2-3-0-57-219.ap-southeast-1.compute.amazonaws.com/)

[Dockerhub URL](https://hub.docker.com/r/samuellws/flask-app/tags)

```

## Details on chosen final model and model parameters

```
CatBoostClassifier(
    learning_rate=0.1, 
    l2_leaf_reg=3,
    iterations=100,
    depth=5,
    border_count=50,
    bagging_temperature=0.3,
    random_state=42, 
    verbose=0)

```

## Offline AUC metric of chosen final model

```
 CatBoostClassifier
 AUC: 0.86578
 Accuracy: 0.8122020972354623

```
