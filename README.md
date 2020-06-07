### <u>Spotify Genre Classification</u>

This project's goal was to serve as my introduction to machine learning. In this project, I attempt to accurately predict a songs genre based on qualities of the song sourced from Spotify's API https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/.

---
### Key Takaways
* While many of the song qualities do a very good job of predicting genre, the performance suffers on the prediction of a specific genre. For example, the model is not great at predicting pop music versus rap music (see confusion matrix). One way of improving the model could be the addition of more data <i>ex. lyrics, frequency, midi arrangement, etc.</i>

<p align="center">
  <img src="https://github.com/abelpd/Spotify_Genre_Classification_Model/blob/master/Machine%20Learning/confusion_matrix.png" width="600" />
</p>

* Bagging & boosting methods produced similar results (performance wise). However, the random forest model was marginally better. Furthermore, the random forest model is better at interpolating feature importance than Adaboost. For these reasons, the random forest was selected. With the addition of new data however, it would be important to retest all models due to the chance a different model performs better at higher dimensions.

* The importance of abstracting the model to improve readability & brevity. One of the mistakes I made in creating this notebook was writing each model in a separate section. A more efficient method would be to abstract the model running to a helper function and run all transformations through an sklearn pipeline. This would substantially decrease the length of the notebook and reduce the time it takes for someone reading my code to understand what I've done. In my second capstone, this is something I will make a point to improve on.


---


<b>For the machine learning code, refer <a href=https://github.com/abelpd/Spotify_Genre_Classification_Model/blob/master/Machine%20Learning/Machine%20Learning-V2.ipynb> to this Jupyter Notebook.</a></b>

<b>For specifics on the project, refer <a href=https://github.com/abelpd/Spotify_Genre_Classification_Model/blob/master/Capstone_Report.pdf> to the final report.</a></b>

---
