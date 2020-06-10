from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import viewsets, status
from .models import MPG
from .serializers import mpgSerializer


# ML imports
import pandas as pd
import joblib
import keras
import numpy as np

# global loads
# Load the model, the data pipeline and the target scaler
loaded_model = keras.models.load_model('./ml_model/MPG_keras_NN')
loaded_pipeline = joblib.load('./ml_model/data_pipeline.pkl')
loaded_target_scaler = joblib.load('./ml_model/target_scaler.pkl')


# Helper functions
def get_input_set(input_dict, load_pipeline):
    # prepare input data
    temp_data = pd.DataFrame({'x': input_dict}).transpose()
    temp_data = temp_data.apply(pd.to_numeric)
    temp_scaled = load_pipeline.transform(temp_data)[:, 1:]
    return temp_scaled


def get_prediction(load_model, load_target_scaler, input_feature_set):
    return float(np.squeeze(load_target_scaler.inverse_transform(load_model.predict(input_feature_set))))


# Create your views here.
class MPGView(viewsets.ModelViewSet):
    queryset = MPG.objects.all()
    serializer_class = mpgSerializer


@api_view(["POST"])
def mpg_predict(request):

    input_values = request.data
    print(input_values)
    model_input = get_input_set(input_values, loaded_pipeline)
    input_post = MPG(
                    acceleration=input_values['acceleration'],\
                    cylinders= input_values['cylinders'],
                    displacement= input_values['displacement'],
                    horsepower= input_values['horsepower'],
                    model_year= input_values['model year'],
                    origin= input_values['origin'],
                    weight= input_values['weight']
                     )
    #input_post.save()
    #print(input_post)
    prediction = get_prediction(loaded_model, loaded_target_scaler, model_input)
    #print(prediction)
    return JsonResponse('Miles per Gallon for your car is: {}'.format(prediction), safe=False)