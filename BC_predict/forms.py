from django import forms

class CancerPredictionForm(forms.Form):
        
    radius_mean = forms.FloatField(
        label='Radius Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 30.0, 'step': 0.01})
    )
    texture_mean = forms.FloatField(
        label='Texture Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 40.0, 'step': 0.01})
    )
    perimeter_mean = forms.FloatField(
        label='Perimeter Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 200.0, 'step': 0.01})
    )
    area_mean = forms.FloatField(
        label='Area Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 2500.0, 'step': 0.01})
    )
    smoothness_mean = forms.FloatField(
        label='Smoothness Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.2, 'step': 0.01})
    )
    compactness_mean = forms.FloatField(
        label='Compactness Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.35, 'step': 0.01})
    )
    concavity_mean = forms.FloatField(
        label='Concavity Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.45, 'step': 0.01})
    )
    concave_points_mean = forms.FloatField(
        label='Concave Points Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.2, 'step': 0.01})
    )
    symmetry_mean = forms.FloatField(
        label='Symmetry Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.4, 'step': 0.01})
    )
    fractal_dimension_mean = forms.FloatField(
        label='Fractal Dimension Mean',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.1, 'step': 0.01})
    )
    radius_se = forms.FloatField(
        label='Radius SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 5.0, 'step': 0.01})
    )
    texture_se = forms.FloatField(
        label='Texture SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 5.0, 'step': 0.01})
    )
    perimeter_se = forms.FloatField(
        label='Perimeter SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 20.0, 'step': 0.01})
    )
    area_se = forms.FloatField(
        label='Area SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 500.0, 'step': 0.01})
    )
    smoothness_se = forms.FloatField(
        label='Smoothness SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.05, 'step': 0.01})
    )
    compactness_se = forms.FloatField(
        label='Compactness SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.1, 'step': 0.01})
    )
    concavity_se = forms.FloatField(
        label='Concavity SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.2, 'step': 0.01})
    )
    concave_points_se = forms.FloatField(
        label='Concave Points SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.05, 'step': 0.01})
    )
    symmetry_se = forms.FloatField(
        label='Symmetry SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.1, 'step': 0.01})
    )
    fractal_dimension_se = forms.FloatField(
        label='Fractal Dimension SE',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.03, 'step': 0.01})
    )
    radius_worst = forms.FloatField(
        label='Radius Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 50.0, 'step': 0.01})
    )
    texture_worst = forms.FloatField(
        label='Texture Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 60.0, 'step': 0.01})
    )
    perimeter_worst = forms.FloatField(
        label='Perimeter Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 300.0, 'step': 0.01})
    )
    area_worst = forms.FloatField(
        label='Area Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 4000.0, 'step': 0.01})
    )
    smoothness_worst = forms.FloatField(
        label='Smoothness Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.2, 'step': 0.01})
    )
    compactness_worst = forms.FloatField(
        label='Compactness Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 1.5, 'step': 0.01})
    )
    concavity_worst = forms.FloatField(
        label='Concavity Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 1.5, 'step': 0.01})
    )
    concave_points_worst = forms.FloatField(
        label='Concave Points Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.5, 'step': 0.01})
    )
    symmetry_worst = forms.FloatField(
        label='Symmetry Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.7, 'step': 0.01})
    )
    fractal_dimension_worst = forms.FloatField(
        label='Fractal Dimension Worst',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0.0, 'max': 0.2, 'step': 0.01})
    )