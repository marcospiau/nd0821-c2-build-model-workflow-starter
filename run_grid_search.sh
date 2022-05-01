mlflow run . \
  -P steps=train_random_forest \
  -P hydra_options="modeling.random_forest.max_depth=1,2,4,8 modeling.random_forest.n_estimators=100,200,500 modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m"
  # -P hydra_options="hydra/launcher=joblib modeling.random_forest.max_depth=1,2,4,8 modeling.random_forest.n_estimators=100,200,500 modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m"
