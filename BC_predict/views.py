from django.shortcuts import render
from .forms import CancerPredictionForm
from .ml_model import predict

def home(request):
    return render(request, 'home.html')

def classify_breast_cancer(request):
    prediction = None
    if request.method == 'POST':
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            features = [
                form.cleaned_data['radius_mean'],
                form.cleaned_data['texture_mean'],
                form.cleaned_data['perimeter_mean'],
                form.cleaned_data['area_mean'],
                form.cleaned_data['smoothness_mean'],
                form.cleaned_data['compactness_mean'],
                form.cleaned_data['concavity_mean'],
                form.cleaned_data['concave_points_mean'],
                form.cleaned_data['symmetry_mean'],
                form.cleaned_data['fractal_dimension_mean'],
                form.cleaned_data['radius_se'],
                form.cleaned_data['texture_se'],
                form.cleaned_data['perimeter_se'],
                form.cleaned_data['area_se'],
                form.cleaned_data['smoothness_se'],
                form.cleaned_data['compactness_se'],
                form.cleaned_data['concavity_se'],
                form.cleaned_data['concave_points_se'],
                form.cleaned_data['symmetry_se'],
                form.cleaned_data['fractal_dimension_se'],
                form.cleaned_data['radius_worst'],
                form.cleaned_data['texture_worst'],
                form.cleaned_data['perimeter_worst'],
                form.cleaned_data['area_worst'],
                form.cleaned_data['smoothness_worst'],
                form.cleaned_data['compactness_worst'],
                form.cleaned_data['concavity_worst'],
                form.cleaned_data['concave_points_worst'],
                form.cleaned_data['symmetry_worst'],
                form.cleaned_data['fractal_dimension_worst'],
            ]
            # Get the prediction from the model
            prediction = predict(features)
    else:
        form = CancerPredictionForm()

    return render(request, 'classify.html', {'form': form, 'prediction': prediction})
